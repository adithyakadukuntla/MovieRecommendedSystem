# -*- coding: utf-8 -*-
"""
Created on Thu May 30 15:05:23 2024

@author: Lenovo
"""


import pickle
import pandas as pd
import difflib
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('movies_Recom.csv')
movie_similarity = pickle.load(open('movie_similarity.sav','rb'))
list_of_movies = pickle.load(open('all_movies.sav','rb'))

movie_name = input(' Enter your favourite movie name : ')

find_close_match = difflib.get_close_matches(movie_name,list_of_movies)

close_matched = find_close_match[0]

index_of_movie  = df[df.title==close_matched]['index'].values[0]

similarity_score = list(enumerate(movie_similarity[index_of_movie]))

sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1], reverse = True) 
# print the name of similar movies based on the index

print('Movies suggested for you : \n')

i = 1
movies_list=[]
for movie in sorted_similar_movies:
  index = movie[0]
  title_from_index = df[df.index==index]['title'].values[0]
  if (i<11):
    #print(i, '.',title_from_index)
    movies_list.append(title_from_index)
    i+=1
    
for i in movies_list:
    print(i)

