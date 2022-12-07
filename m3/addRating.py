################################
## MILESTONE 3 - IMPROVEMENTS ##
################################

# Import libraries
import pandas as pd
import re

def readTitles(all_movies):
    titlesIMDB = pd.read_csv('data/imdbDatasets/dataNames.tsv', sep='\t', low_memory=False)
    ratings = pd.read_csv('data/imdbDatasets/dataRating.tsv', sep='\t')


    # ratings

    # new_df = pd.merge(A_df, B_df,  how='left', left_on=['A_c1','c2'], right_on = ['B_c1','c2'])
    all_movies = pd.merge(all_movies, titlesIMDB[['tconst','Title']], how='left', on='Title')
    # Drop column with the new id
    all_movies.drop(columns='id', axis=1, inplace=True)
    all_movies.drop_duplicates(subset="Title", inplace=True)

    all_movies = pd.merge(all_movies, ratings[['tconst', 'averageRating']], how="left", on='tconst')
    all_movies.drop(columns='tconst', axis=1, inplace=True)

    # print(all_movies.head())
    return all_movies


if __name__ == '__main__' :
    all_movies = pd.read_csv('data/wiki_movie_plots.csv', sep=',')
    all_movies = readTitles(all_movies)

    all_movies.to_csv('data/wiki_movie_final.csv', sep=',')
