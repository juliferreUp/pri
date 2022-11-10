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
    words_to_remove = ['about','age','ago','african','and', 'based','bond','bros.','can','chan','coming','com','comedey','crime.','das','day','direct','dwayne','early','family.','familya','fiction','for','found','from','genre','given','human','into','james','johansson','johnson','kung','loosely','made','munro.','name','name.','not','panorama','period','p.o.w.','produced','production','productions','related','rights','road','same','scarllet','sci','semi','set','south','stop','studios','the','thriler','time','triller','true','ttriller','warner','with','years','yeh']
    for row in all_movies['Genre']:
        row = re.split(',|\s|/|\(|\)|\[|\]|;|-', row)

        # if ('science' in row) and not ('fiction' in row):
        #     print(row)

        if 'comedey' in row:
            row.append('comedy')
        if 'crime.' in row:
            row.append('crime')
        if 'dwayne' in row:
            row.append('dwayne johnson')
        if ('family.' in row) or ('familya' in row):
            row.append('family')
        if 'fi' in row:
            row.append('science fiction')
        if 'fiction' in row:
            row.append('science fiction')
            if 'science' in row:
                row.remove('science')
        if 'humans' in row:
            row.append('human rights')
        if 'james' in row:
            row.append('james bond')
        if 'kung' in row:
            row.append('kung fu')
        if 'panorama' in row:
            row.append('panorama studios')
        if 'p.o.w.' in row:
            row.append('pow')
        if 'scarllet' in row:
            row.append('scarllet johansson')
        if 'south' in row:
            row.append('south african')
        if ('ttriller' in row) or ('triller' in row) or ('thriler' in row):
            row.append('thriller')
        if 'warner' in row:
            row.append('warner bros')

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
    all_movies.to_csv('../m2/data/wiki_movie_plots.csv', sep=',')
