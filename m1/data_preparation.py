####################################
## MILESTONE 1 - DATA PREPARATION ##
####################################

# Import libraries
import pandas as pd
import re

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



def prepare_data(all_movies):

    # Fill NaN values with Unkown

    all_movies['Cast'] = all_movies['Cast'].fillna('Unkown')


    # Convert Genres in a list of Genres
    # Example: [romantic drama] -> [romatic, drama] 

    genre_f = []
    words_to_remove = ['age','ago','and','based','can','coming','das','day','from','given','into','not','semi','stop','the','time','true','with','years','yeh']
    for row in all_movies['Genre']:
        row = re.split(',|\s|/|\(|\)|\[|\]|;|-', row)
        genre_f.append(list(filter(lambda x: len(x) >= 3 and not x.isdigit() and not (x in words_to_remove), row)))
        # print(row)
    all_movies['Genre'] = genre_f
    
    # print(all_movies['Genre'])
    # print(unique_g(all_movies['Genre']))
    # print(len(unique_g(all_movies['Genre'])))


    # Remove Origin's movies with less than 10 movies

    origins_array = unique(all_movies['Origin/Ethnicity'])
    remove_origins = []
    for i in origins_array:
        if (len(all_movies[all_movies['Origin/Ethnicity']==i]) < 10) :
            # print(i, '-', len(all_movies[all_movies['Origin/Ethnicity']==i]))
            remove_origins.append(i)
    # print(remove_origins)
    for i in remove_origins:
        all_movies.drop(all_movies.index[(all_movies["Origin/Ethnicity"] == i)],axis=0,inplace=True)

    return all_movies



if __name__ == '__main__':
    # Load dataset
    all_movies = pd.read_csv('data/wiki_movie_plots_deduped.csv', sep=',')
    all_movies = prepare_data(all_movies)
    # Store dataset
    all_movies.to_csv('data/wiki_movie_plots.csv', sep=',')
