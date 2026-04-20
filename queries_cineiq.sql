CREATE DATABASE IF NOT EXISTS cineiq_db;
USE cineiq_db;
CREATE TABLE IF NOT EXISTS movies (
    id INT PRIMARY KEY,
    title VARCHAR(500),
    overview TEXT,
    genres VARCHAR(500),
    vote_average FLOAT,
    vote_count INT,
    popularity FLOAT,
    release_date VARCHAR(50),
    runtime FLOAT,
    original_language VARCHAR(20),
    keywords VARCHAR(1000)
);
USE cineiq_db;
SELECT COUNT(*) FROM movies;

USE cineiq_db;

-- Query 1: Top 10 highest rated movies (min 100 votes for credibility)
SELECT title, vote_average, vote_count, genres
FROM movies
WHERE vote_count >= 100
ORDER BY vote_average DESC
LIMIT 10;

-- Query 2: Most popular genres
SELECT genres, COUNT(*) as movie_count,
ROUND(AVG(vote_average), 2) as avg_rating
FROM movies
WHERE genres != ''
GROUP BY genres
ORDER BY movie_count DESC
LIMIT 10;

-- Query 3: Best movies by decade
SELECT 
    CONCAT(FLOOR(YEAR(release_date)/10)*10, 's') as decade,
    COUNT(*) as total_movies,
    ROUND(AVG(vote_average), 2) as avg_rating,
    ROUND(AVG(popularity), 2) as avg_popularity
FROM movies
WHERE release_date IS NOT NULL
GROUP BY decade
ORDER BY decade;

-- Query 4: Top languages by movie count
SELECT original_language,
COUNT(*) as movie_count,
ROUND(AVG(vote_average), 2) as avg_rating
FROM movies
GROUP BY original_language
ORDER BY movie_count DESC
LIMIT 10;

-- Query 5: Movies with highest popularity scores
SELECT title, popularity, vote_average, genres
FROM movies
ORDER BY popularity DESC
LIMIT 10;

-- Query 6: Runtime analysis
SELECT 
    CASE 
        WHEN runtime < 60 THEN 'Short (<1hr)'
        WHEN runtime BETWEEN 60 AND 120 THEN 'Standard (1-2hr)'
        WHEN runtime BETWEEN 120 AND 180 THEN 'Long (2-3hr)'
        ELSE 'Epic (3hr+)'
    END as runtime_category,
    COUNT(*) as movie_count,
    ROUND(AVG(vote_average), 2) as avg_rating
FROM movies
WHERE runtime > 0
GROUP BY runtime_category
ORDER BY avg_rating DESC;

-- Query 7: Top rated movies per language (simplified)
SELECT 
    original_language,
    COUNT(*) as total_movies,
    ROUND(AVG(vote_average), 2) as avg_rating,
    ROUND(MAX(vote_average), 2) as highest_rating,
    ROUND(AVG(popularity), 2) as avg_popularity
FROM movies
WHERE vote_count >= 50
AND original_language IN ('en', 'fr', 'es', 'hi', 'ja', 'ko', 'de', 'it', 'pt', 'zh')
GROUP BY original_language
ORDER BY avg_rating DESC;

-- Query 8: Yearly movie production trend
SELECT 
    YEAR(release_date) as year,
    COUNT(*) as movies_released,
    ROUND(AVG(vote_average), 2) as avg_rating
FROM movies
WHERE release_date IS NOT NULL
AND YEAR(release_date) BETWEEN 2000 AND 2024
GROUP BY year
ORDER BY year;