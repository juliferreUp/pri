####################################
## MILESTONE 3 - CHANGES         ##
####################################

# Import libraries
import pandas as pd
import re

def readTitles(all_movies):
    titlesIMDB = pd.read_csv('data/dataNames.tsv', sep='\t')
    ratings = pd.read_csv('data/dataRating.tsv', sep='\t')


    # ratings
    all_movies = pd.merge(all_movies, titlesIMDB[['tconst','Title']], on='Title')
    # Drop column with the new id
    all_movies.drop(columns='id', axis=1, inplace=True)

    all_movies = pd.merge(all_movies, ratings[['tconst', 'averageRating']], on='tconst')
    all_movies.drop(columns='tconst', axis=1, inplace=True)

    print(all_movies.head())
    return all_movies


if __name__ == '__main__' :
    all_movies = pd.read_csv('data/wiki_movie_plots.csv', sep=',')
    all_movies = readTitles(all_movies)

    all_movies.to_csv('data/wiki_movie_final.csv', sep=',')
