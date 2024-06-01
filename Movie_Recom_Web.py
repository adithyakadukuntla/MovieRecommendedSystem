# -*- coding: utf-8 -*-
"""
Created on Thu May 30 15:13:43 2024

@author: Lenovo
"""

import pickle
import requests
import pandas as pd
import streamlit as st
import difflib
import warnings
warnings.filterwarnings('ignore')
#"https://github.com/adithyakadukuntla/MovieRecommendedSystem/releases/tag/untagged-9713449c24611040cf77"
file_url = "https://github.com/adithyakadukuntla/MovieRecommendedSystem/releases/download/untagged-9713449c24611040cf77/movie_similarity.sav"

# Download the file from GitHub
response = requests.get(file_url)

# Save the file locally
with open('movie_similarity.sav', 'wb') as f:
    f.write(response.content)

df = pd.read_csv('movies_Recom.csv')
movie_similarity = pickle.load(open('movie_similarity.sav','rb'))
list_of_movies = pickle.load(open('all_movies.sav','rb'))




def Recomend_Movie(input_data):
    movie_name = input_data

    find_close_match = difflib.get_close_matches(movie_name,list_of_movies)

    close_matched = find_close_match[0]

    index_of_movie  = df[df.title==close_matched]['index'].values[0]

    similarity_score = list(enumerate(movie_similarity[index_of_movie]))

    sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1], reverse = True) 
    # print the name of similar movies based on the index

    

    i = 1
    movies_list =[]
    for movie in sorted_similar_movies:
      index = movie[0]
      
      title_from_index = df[df.index==index]['title'].values[0]
      if (i<11):
        #print(i, '.',title_from_index)
        movies_list.append(title_from_index)
        i+=1
    return movies_list
        
def main():
    st.title("Movie Recommended System")
    st.balloons()
    movie = st.text_input('Movie name : ')
    
    
    movies= []
    
    
    if st.button('Recommend Movies'):
        movies = Recomend_Movie(movie)
        
    if len(movies) > 0:
        st.success('Movie Recommended for You:')
        st.markdown('\n'.join(f"- {movie}" for movie in movies))
        


    if(len(movies)==0):
        st.warning('No Movies are Recommended')
        
        
        
if __name__ == '__main__':
    main()    
    
