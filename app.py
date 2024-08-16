import streamlit as st
import pickle 
import pandas as pd

def recommend(movie):
    movie_index=movies[movies["title"]==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    rec_movies=[]
    for i in movies_list:
        rec_movies.append(movies.iloc[i[0]].title)
    return rec_movies

movies_list=pickle.load(open("movie_dict.pkl","rb"))
movies=pd.DataFrame(movies_list)

similarity=pickle.load(open("similarity.pkl","rb"))
st.title("Movie Recommender System")

option = st.selectbox("How would you like to be contacted?",
movies["title"].values)

if st.button("Recommend"):
    rec=recommend(option)
    for i in rec:
        st.write(i)

