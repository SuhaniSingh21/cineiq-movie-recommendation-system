import pandas as pd

# Load dataset
print("Loading dataset... please wait")
df = pd.read_csv("C:/Users/suhan/cineiq/data/TMDB_movie_dataset_v11.csv")
print(f"✅ Loaded! Total movies: {len(df)}")

# Step 1 - Keep only useful columns
columns_needed = ['id', 'title', 'overview', 'genres', 'vote_average', 
                  'vote_count', 'popularity', 'release_date', 'runtime',
                  'original_language', 'keywords']
df = df[columns_needed]
print(f"\n✅ Kept only useful columns: {list(df.columns)}")

# Step 2 - Drop rows where title or overview is missing
df = df.dropna(subset=['title', 'overview'])
print(f"✅ After removing missing titles/overviews: {len(df)} movies")

# Step 3 - Fill missing genres and keywords with empty string
df['genres'] = df['genres'].fillna('')
df['keywords'] = df['keywords'].fillna('')

# Step 4 - Keep only movies with at least 10 votes (remove junk)
df = df[df['vote_count'] >= 10]
print(f"✅ After removing low-vote movies: {len(df)} movies")

# Step 5 - Save cleaned data
df.to_csv("C:/Users/suhan/cineiq/data/tmdb_cleaned.csv", index=False)
print(f"\n🎉 Cleaned dataset saved!")
print(f"Final dataset: {len(df)} movies ready for recommendation engine")