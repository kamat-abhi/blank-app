import streamlit as st
import pickle
import pandas as pd

movie_list = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_list)

similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(movie_name):  
        movie_index = movies[movies['title']==movie_name].index[0]
        distances= similarity[movie_index]
        movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

        recommendations = []
        for i in movies_list:
            movie_id = i[0]
            recommendations.append(movies.iloc[i[0]].title)

        return recommendations



st.title("🎬 Movie Recommender System")


st.write(
    "Welcome to the Movie Recommendation System! 🎥\n"
    "To get started, select a movie you like from the dropdown below.\n"
    "Based on your selection, we'll suggest similar movies you might enjoy.\n"
    "Just pick one and let us do the magic! ✨"
)

selected_movie = st.selectbox(
    'Select a movie to get recommendations:',
    movies['title'].values)

if st.button('Recommend'):
    recomend_movie = recommend(selected_movie )
    for i in recomend_movie:
        st.write(i)
