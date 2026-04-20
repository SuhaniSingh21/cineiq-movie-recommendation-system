import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load cleaned data
print("Loading data...")
df = pd.read_csv("C:/Users/suhan/cineiq/data/tmdb_cleaned.csv")
df = df.dropna(subset=['title', 'overview'])
df = df.reset_index(drop=True)
print(f"✅ {len(df)} movies loaded")

# Combine overview + genres + keywords into one text column
df['combined'] = (
    df['overview'].fillna('') + ' ' +
    df['genres'].fillna('') + ' ' +
    df['keywords'].fillna('')
)

# Build TF-IDF matrix
print("Building recommendation model...")
tfidf = TfidfVectorizer(stop_words='english', max_features=10000)
tfidf_matrix = tfidf.fit_transform(df['combined'])
print(f"✅ Model built! Matrix shape: {tfidf_matrix.shape}")

# Cosine similarity function
def recommend(movie_title, n=10):
    # Find the movie
    matches = df[df['title'].str.lower() == movie_title.lower()]
    
    if matches.empty:
        # Try partial match
        matches = df[df['title'].str.lower().str.contains(movie_title.lower())]
        if matches.empty:
            return f"Movie '{movie_title}' not found!"
    
    idx = matches.index[0]
    movie = df.loc[idx]
    print(f"\n🎬 Because you liked: {movie['title']}")
    print(f"   Genres: {movie['genres']}")
    print(f"   Rating: {movie['vote_average']}")
    
    # Calculate similarity scores
    sim_scores = cosine_similarity(tfidf_matrix[idx], tfidf_matrix).flatten()
    sim_scores[idx] = 0  # exclude the movie itself
    
    # Get top N similar movies
    top_indices = sim_scores.argsort()[-n:][::-1]
    
    print(f"\n🍿 Top {n} recommendations:\n")
    for i, rec_idx in enumerate(top_indices, 1):
        rec = df.loc[rec_idx]
        print(f"{i}. {rec['title']}")
        print(f"   Genres: {rec['genres']} | Rating: {rec['vote_average']} | Similarity: {sim_scores[rec_idx]:.2f}")
        print()
    
    return top_indices

# Test it!
print("\n" + "="*50)
recommend("Inception")
print("="*50)
recommend("The Dark Knight")