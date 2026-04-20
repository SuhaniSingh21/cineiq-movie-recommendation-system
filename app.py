import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Page config
st.set_page_config(
    page_title="CineIQ",
    page_icon="🎬",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #E50914;
    }
    .sub-header {
        font-size: 1.2rem;
        text-align: center;
        color: #888888;
        margin-bottom: 2rem;
    }
    .movie-card {
        background: #1a1a2e;
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
        border-left: 4px solid #E50914;
    }
    .sentiment-positive { color: #00ff88; font-weight: bold; }
    .sentiment-negative { color: #ff4444; font-weight: bold; }
    .sentiment-neutral  { color: #ffaa00; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<p class="main-header">🎬 CineIQ</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Intelligent Movie Recommendation Engine with Sentiment Analysis</p>', unsafe_allow_html=True)

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("C:/Users/suhan/cineiq/data/tmdb_with_sentiment.csv")
    df = df.dropna(subset=['title','overview'])
    df = df.reset_index(drop=True)
    return df

@st.cache_data
def build_model(df):
    df['combined'] = (
        df['overview'].fillna('') + ' ' +
        df['genres'].fillna('') + ' ' +
        df['keywords'].fillna('')
    )
    tfidf = TfidfVectorizer(stop_words='english', max_features=10000)
    matrix = tfidf.fit_transform(df['combined'])
    return matrix

# Load
with st.spinner("Loading CineIQ... please wait"):
    df = load_data()
    matrix = build_model(df)

st.success(f"✅ {len(df):,} movies loaded and ready!")

# ── Sidebar ────────────────────────────────────────────────────────────────
st.sidebar.title("🎛️ Filters")
num_recommendations = st.sidebar.slider("Number of recommendations", 5, 20, 10)
min_rating = st.sidebar.slider("Minimum rating", 0.0, 10.0, 5.0, 0.5)
selected_sentiment = st.sidebar.selectbox(
    "Filter by sentiment",
    ["All", "Positive", "Negative", "Neutral"]
)

# ── Search ─────────────────────────────────────────────────────────────────
st.subheader("🔍 Search a Movie")
movie_input = st.text_input("Type a movie name (e.g. Inception, The Dark Knight, Avengers)")

if movie_input:
    matches = df[df['title'].str.lower().str.contains(movie_input.lower())]
    
    if matches.empty:
        st.error(f"❌ No movie found matching '{movie_input}'")
    else:
        # Show matched movies to select
        movie_titles = matches['title'].tolist()
        selected_title = st.selectbox("Select the exact movie:", movie_titles)
        
        if selected_title:
            idx = df[df['title'] == selected_title].index[0]
            selected_movie = df.loc[idx]
            
            # Show selected movie info
            st.markdown("---")
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("⭐ Rating", f"{selected_movie['vote_average']:.1f}/10")
            with col2:
                st.metric("🗳️ Votes", f"{int(selected_movie['vote_count']):,}")
            with col3:
                st.metric("🎭 Sentiment", selected_movie['sentiment'])
            with col4:
                st.metric("🔥 Popularity", f"{selected_movie['popularity']:.1f}")
            
            st.markdown(f"**Genres:** {selected_movie['genres']}")
            st.markdown(f"**Overview:** {selected_movie['overview']}")
            st.markdown("---")
            
            # Get recommendations
            sim_scores = cosine_similarity(matrix[idx], matrix).flatten()
            sim_scores[idx] = 0
            top_indices = sim_scores.argsort()[-50:][::-1]
            
            recommendations = df.loc[top_indices].copy()
            recommendations['similarity'] = sim_scores[top_indices]
            
            # Apply filters
            recommendations = recommendations[recommendations['vote_average'] >= min_rating]
            if selected_sentiment != "All":
                recommendations = recommendations[recommendations['sentiment'] == selected_sentiment]
            
            recommendations = recommendations.head(num_recommendations)
            
            st.subheader(f"🍿 Top {len(recommendations)} Recommendations for '{selected_title}'")
            
            for i, (_, row) in enumerate(recommendations.iterrows(), 1):
                sentiment_color = {
                    'Positive': '🟢',
                    'Negative': '🔴', 
                    'Neutral': '🟡'
                }.get(row['sentiment'], '⚪')
                
                with st.expander(f"{i}. {row['title']} ⭐ {row['vote_average']:.1f} | {sentiment_color} {row['sentiment']} | Similarity: {row['similarity']:.0%}"):
                    col1, col2 = st.columns([1, 3])
                    with col1:
                        st.metric("Rating", f"{row['vote_average']:.1f}/10")
                        st.metric("Similarity", f"{row['similarity']:.0%}")
                        st.metric("Sentiment Score", f"{row['sentiment_score']:.2f}")
                    with col2:
                        st.markdown(f"**Genres:** {row['genres']}")
                        st.markdown(f"**Overview:** {row['overview'][:300]}...")

# ── Stats section ──────────────────────────────────────────────────────────
st.markdown("---")
st.subheader("📊 Dataset Overview")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Movies", f"{len(df):,}")
with col2:
    st.metric("Positive Movies", f"{(df['sentiment']=='Positive').sum():,}")
with col3:
    st.metric("Negative Movies", f"{(df['sentiment']=='Negative').sum():,}")
with col4:
    st.metric("Avg Rating", f"{df['vote_average'].mean():.2f}")

st.markdown("---")
st.markdown("<p style='text-align:center; color:#888'>Built by Suhani | CineIQ — Intelligent Movie Recommendations</p>", unsafe_allow_html=True)