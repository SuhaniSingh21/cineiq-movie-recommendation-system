# CineIQ: AI-Powered Movie Recommendation & Analytics System

# Overview

CineIQ is a full-stack data science project that delivers intelligent movie recommendations by combining machine learning, NLP, and SQL analytics.

Unlike basic recommendation systems, CineIQ goes beyond similarity matching by integrating:

Content-based filtering
Sentiment-aware recommendations
Data-driven insights using SQL

The result is a multi-layered recommendation engine that is both predictive and explainable.

# Problem Statement

Most movie recommendation systems:

Suggest content based only on similarity
Ignore emotional context
Lack analytical insights

CineIQ solves this by building a system that:

Understands what a movie is about
Considers how it feels (sentiment)
Uses data insights to improve recommendations

# Key Features
🔹 Smart Recommendation Engine
TF-IDF + Cosine Similarity
Uses overview, genres, and keywords
Returns relevant, content-based suggestions

🔹 Sentiment-Aware Filtering
NLP-based sentiment analysis (VADER)
Enhances recommendations using emotional tone

🔹 SQL Analytics Layer
Designed MySQL database for structured storage
Performed analytical queries to extract:
Genre trends
Rating distribution
Language insights
Decade analysis

🔹 Data Engineering Pipeline
Cleaned and processed 77,677+ records
Feature engineering for improved model performance

🔹 Interactive Application
Built with Streamlit
Real-time movie recommendations
Clean and user-friendly UI

# System Architecture
Raw Dataset  
   ↓  
Data Cleaning & Preprocessing  
   ↓  
Feature Engineering  
   ↓  
Recommendation Engine (TF-IDF + Cosine Similarity)  
   ↓  
Sentiment Analysis (NLP)  
   ↓  
SQL Analytics Layer  
   ↓  
Streamlit Web Application  

# Tech Stack

🔹 Programming
Python

🔹 Libraries
Pandas, NumPy
Scikit-learn
NLTK (VADER)

🔹 Database
MySQL
SQLAlchemy

🔹 Visualization & App
Streamlit

# Key Insights
High popularity ≠ high rating
Drama & thriller genres dominate high ratings
English movies dominate volume, but regional films often score higher
Optimal runtime (~90–120 mins) correlates with better ratings

# Sample Analysis
Top-rated movies (credibility filtered)
Genre distribution trends
Decade-wise movie performance
Language-based insights

# Getting Started
1️. Clone the Repository
git clone https://github.com/SuhaniSingh21/cineiq-movie-recommendation-system
cd cineiq-movie-recommendation-system
2️. Install Dependencies
pip install -r requirements.txt
3️. Setup Environment Variables

Create a .env file:

DB_USER=your_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=3306
DB_NAME=cineiq_db
4️. Run the Application
streamlit run app.py

# Project Structure
cineiq/
│── data/                # Raw & cleaned datasets  
│── eda.py               # Data preprocessing  
│── load.py              # Database loading  
│── recommend.py         # Recommendation logic  
│── sentiment.py         # NLP sentiment analysis  
│── app.py               # Streamlit app  
│── queries.sql          # SQL analytics  
│── README.md  

 # Project Highlights

1. End-to-end data pipeline
2. Integration of ML + NLP + SQL
3. Real-world dataset handling
4. Modular code architecture
5.  Interactive web application

# Future Improvements
Hybrid recommender (content + collaborative filtering)
User-based personalization
Model evaluation metrics (Precision@K, Recall)
Cloud deployment

# Author
Suhani Singh
Aspiring Data Analyst | Data Science Enthusiast
