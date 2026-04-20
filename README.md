# cineiq-movie-recommendation-system
AI-powered movie recommendation engine with sentiment analysis on 77,677 movies.

CineIQ: Intelligent Movie Recommendation & Analytics System

# Overview:
CineIQ is an end-to-end data-driven movie recommendation system that combines content-based filtering, sentiment analysis, and SQL-driven analytics to deliver personalized and insight-rich movie suggestions.

Unlike traditional recommenders, CineIQ enhances recommendations by integrating text similarity, user sentiment, and data insights, making it more context-aware and analytically robust.

# Problem Statement

Modern streaming platforms often rely on basic recommendation logic that:
Ignores user sentiment Lacks explainability
Does not leverage deeper data insights

CineIQ addresses this by building a multi-layered recommendation system that combines machine learning with analytical intelligence.

# Key Features
🔹 Intelligent Recommendation Engine
Built using TF-IDF Vectorization + Cosine Similarity
Recommends movies based on content similarity (overview, genres, keywords)

🔹 Sentiment Analysis Integration
Uses VADER NLP to analyze movie descriptions
Enhances recommendations based on emotional tone

🔹 SQL-Based Data Analytics
Designed a structured MySQL database
Performed advanced queries to extract insights:
Genre popularity trends
Language distribution
Rating patterns
Decade-wise analysis

🔹 Data Processing Pipeline
Cleaned and transformed 10,000+ movie records
Feature engineering for improved recommendation quality

🔹 Interactive Web Application
Built using Streamlit
Real-time movie recommendations with user-friendly interface

# System Architecture
Raw Dataset → Data Cleaning → Feature Engineering →  Recommendation Engine → Sentiment Analysis →  SQL Analytics → Streamlit Application

# Tech Stack
Programming & Libraries
Python (Pandas, NumPy, Scikit-learn)
NLP (VADER)
Data & Database
MySQL
SQLAlchemy
Visualization & App
Streamlit
Concepts Used
Content-Based Filtering
Natural Language Processing (NLP)
Data Cleaning & EDA
SQL Analytics

# Key Insights from Data
High-rated movies often belong to drama and thriller genres
Popularity does not always correlate with higher ratings
English-language movies dominate dataset, but regional films show strong ratings
Movies with moderate runtime (~90–120 mins) tend to perform better

# Sample SQL Analysis
Top-rated movies with credibility filtering
Genre-wise movie distribution
Decade-based trend analysis
Runtime segmentation insights

# How to Run the Project
1. Clone Repository
git clone https://github.com/SuhaniSingh21/cineiq-movie-recommendation-system
cd cineiq-movie-recommendation-system
2. Install Dependencies
pip install -r requirements.txt
3. Setup Environment Variables

Create a .env file:

DB_USER=your_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=3306
DB_NAME=cineiq_db
4. Run Application
streamlit run app.py

# Project Highlights

✔ End-to-end data pipeline
✔ Integration of ML + NLP + SQL
✔ Real-world dataset handling
✔ Modular and scalable code structure
✔ Interactive application deployment

# Future Enhancements
Hybrid recommendation system (content + collaborative filtering)
User-based personalization
Real-time data integration
Advanced model evaluation metrics

# Author
Suhani Singh
Aspiring Data Analyst | Data Science Enthusiast
