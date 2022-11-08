#################################
## MILESTONE 1 - DATA ANALYSIS ##
#################################

# Import libraries
import pandas as pd
from data_preparation import prepare_data

# Auxiliar functions

def unique(list1):
    response_list = []
    # insert the list to the set
    list_set = set(list1)
    # convert the set to the list
    unique_list = (list(list_set))
    for x in unique_list:
        response_list.append(x)
    return response_list 

def unique_g(list1):
    response_list = []
    for r in list1:
        for i in r:
            if not i in response_list:
                response_list.append(i)
    return response_list


# Data preparation
all_movies = pd.read_csv('data/wiki_movie_plots_deduped.csv', sep=',')
all_movies = prepare_data(all_movies)


# Data statistics
print(all_movies.shape)
print(all_movies.info())

# Total number of movies
print(len(all_movies), 'movies')

# Older and newer movie
first = all_movies['Release Year'].min()
last = all_movies['Release Year'].max()
print('Movies betweeen', first, 'and', last)

# Total number of origins/ethnicities
print(len(unique(all_movies['Origin/Ethnicity'])), 'different origins/ethinities')
print(unique(all_movies['Origin/Ethnicity']))

# Total number of genres
# print(unique_g(all_movies['Genre']))
print(len(unique_g(all_movies['Genre'])), 'genres')

