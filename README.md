# 🎬 Movie Recommendation System

This project is a **Content-Based Movie Recommender** built using Python. It suggests movies similar to a selected one based on a dataset of 5000 movies.

## 🚀 Features

- Recommend 5 similar movies to a selected title
- Uses cosine similarity for recommendation
- Interactive UI built with Streamlit
- Lightweight and fast (uses a precomputed similarity matrix)

## 📁 Dataset

- Contains information about 5000 movies (title, genres, overview, etc.)
- Loaded from a local CSV file or Pickle format

## 🧠 How It Works

1. Feature extraction from movie descriptions
2. Vectorization using `TfidfVectorizer` or `CountVectorizer`
3. Compute cosine similarity between movie vectors
4. Recommend top 5 most similar movies (excluding the selected one)


## 🛠 Tech Stack

- Python 🐍
- Pandas & NumPy
- Scikit-learn
- Streamlit (for UI)
- Pickle (for saving similarity matrix and data)

## 🧾 Requirements

Install dependencies:

```bash
pip install -r requirements.txt


### How to run it on your own machine

1. Install the requirements

   ```
   $ pip install -r requirements.txt
   ```

2. Run the app

   ```
   $ streamlit run streamlit_app.py
   ```
