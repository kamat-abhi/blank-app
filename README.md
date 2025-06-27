# 🎬 Movie Recommendation System

This project is a **Content-Based Movie Recommender** built using Python. It suggests movies similar to a selected one based on a dataset of 7000 movies.

---

## 🚀 Features

- Recommend 5 similar movies to a selected title
- Uses cosine similarity for recommendation
- Interactive UI built with Streamlit
- Lightweight and fast (uses a precomputed similarity matrix)
  
---

## 🛠️ How I Built This App

### 🔄 1. Data Collection & Exploration
- Collected data from a movie dataset (CSV format).
- Loaded the dataset using `pandas`.
- Explored columns like `title`, `genres`, `overview` etc.

### 🧹 2. Data Preprocessing
- Cleaned the data (e.g., removed nulls, duplicates).
- Combined important features like overview, genres, etc., into a single string for vectorization.

### 📐 3. Feature Extraction
- Used **TF-IDF Vectorizer** or **CountVectorizer** to convert text to numerical format.
- Calculated **cosine similarity** to compare movies.

### 🤖 4. Recommendation Logic
- Wrote a `recommend(movie_name)` function to:
  - Find the movie index
  - Compute similarity scores
  - Sort and recommend top 5 similar movies

### 💾 5. Model & Data Storage
- Saved the movie dictionary and similarity matrix as `.pkl` using `pickle`.
- Loaded them during app runtime for fast execution.

### 🎨 6. App Interface (Frontend)
- Created a UI with **Streamlit**:
  - Dropdown to select a movie
  - Display of recommended movie titles and posters

### 🚀 7. Deployment
- Deployed the app using **Streamlit Cloud**.
- Version control and collaboration managed using GitHub.

---

## 📁 Dataset

- Contains information about 7000 movies (title, genres, overview, etc.)
- Loaded from a local CSV file or Pickle format
- 📊 **Source**: Dataset obtained from [Kaggle - The Movies Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
- 📦 **Dataset Name**: The Movies Dataset by [tmdb_5000_movies, tmdb_5000_credits, IMDB-Movie-Dataset(2023-1951)]

---

## 🛠 Tech Stack

- Python 🐍
- Pandas & NumPy
- Scikit-learn
- Streamlit (for UI)
- Pickle (for saving similarity matrix and data)

 ---

## 🚧 Future Improvements

- Add collaborative filtering
- Include movie poster thumbnails
- Add search filter and UI improvements
- Dockerize for flexible deployment
- Integrate with FastAPI backend for model serving

 ---
 
## 📎 How to Run Locally

```bash
# Clone the repo
git clone https://github.com/kamat-abhi/blank-app.git
cd blank-app

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

---

## 📑 License

This project is under the MIT License.
