import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

# Password with special characters handled safely
password = quote_plus("SuH@nI00")

print("Connecting to MySQL...")
engine = create_engine(f'mysql+mysqlconnector://root:{password}@127.0.0.1:3306/cineiq_db')
print("✅ Connected!")

print("Loading cleaned CSV...")
df = pd.read_csv("C:/Users/suhan/cineiq/data/tmdb_cleaned.csv")
print(f"✅ {len(df)} movies loaded")

print("Inserting into MySQL... (5-10 mins)")
df.to_sql('movies', con=engine, if_exists='replace', 
          index=False, chunksize=1000)

print("🎉 Done! All movies inserted!")