# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 15:54:43 2022

@author: DELL
"""

import streamlit as st
import pandas
import pickle
import requests

movies_list=pickle.load(open('movies.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))
popularity=pickle.load(open('popularity.pkl','rb'))

movies_lis=movies_list['title'].values
recommended_movies=[]
poster=[]

def recommend(X):
    
    movie_index=movies_list[movies_list['title']==X].index[0]
    dist=similarity[movie_index]
    movies_li=sorted(list(enumerate(dist)),reverse=True,key=lambda x:x[1])[1:6]
    #print(movies_li)
    
    for i in movies_li:
        poster.append(fetch_posters(movies_list.iloc[i[0]].movie_id))
        recommended_movies.append(movies_list.iloc[i[0]].title)
    return recommended_movies,poster


def fetch_posters(ide):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=5757f017f191035c7d89a69ff49dcd15&language=en-US".format(ide)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path
   

#print(movies_list)
st.title('Movie Recommender System')

option = st.selectbox(
     'How would you like to be contacted?',
    movies_lis)

st.write('You selected:', option)

    
if st.button('Recommend'):
     r,p=recommend(option)
    
     col1, col2, col3, col4, col5 = st.columns(5)
     with col1:
        st.text(r[0])
        st.image(p[0])
     with col2:
        st.text(r[1])
        st.image(p[1])

     with col3:
        st.text(r[2])
        st.image(p[2])
     with col4:
        st.text(r[3])
        st.image(p[3])
     with col5:
        st.text(r[4])
        st.image(p[4])



st.subheader("Top Movies based on Popularity")
pop_id=popularity['id']
pop_movie=popularity['original_title']
pop_movies_posters=[]
pop_movies_name=[]
for i in pop_movie:
    pop_movies_name.append(i)
for i in pop_id:
    pop_movies_posters.append(fetch_posters(i))
    
#print(pop_movies_posters)
col5, col6, col7, col8, col9 = st.columns(5)
with col5:
        st.text(pop_movies_name[0])
        st.image(pop_movies_posters[0])
with col6:
        st.text(pop_movies_name[1])
        st.image(pop_movies_posters[1])

with col7:
        st.text(pop_movies_name[2])
        st.image(pop_movies_posters[2])
with col8:
        st.text(pop_movies_name[3])
        st.image(pop_movies_posters[3])
with col9:
        st.text(pop_movies_name[4])
        st.image(pop_movies_posters[4])




