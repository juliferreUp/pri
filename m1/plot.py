########################
## MILESTONE 1 - PLOT ##
########################

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from collections import Counter
from data_preparation import prepare_data


pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)



def plot_movies_decade(movies):
    min_year = movies["Release Year"].min()
    max_year = movies["Release Year"].max()
    movies_year_serie = movies["Release Year"].groupby(pd.cut(movies["Release Year"], np.arange(min_year, max_year, 10))).count()

    plt.rcParams.update({"font.size": 16})
    plt.ylabel("Nº movies")
    plt.title("Movies per Decade")

    movies_year_serie.plot.bar()

    fig = matplotlib.pyplot.gcf()
    fig.set_size_inches(18.5, 16.5)
    fig.savefig('images/plot/movies_decade.png')
    plt.clf()


def circular_plot_genre(movies):
    # create serie to plot
    # movies_genre = movies["Genre"].groupby(movies["Genre"]).count()
    genre_dict = {}
    for row in movies["Genre"]:
        for genre in row:
            if genre in genre_dict:
                genre_dict[genre] += 1
            else:
                genre_dict[genre] = 1
    
    # print(genre_dict)

    new_genre_dict = {}
    new_genre_dict["Others"] = 0
    for genre in list(genre_dict):
        if genre_dict[genre] < 1000:
            new_genre_dict["Others"] += 1
        else:
            new_genre_dict[genre] = genre_dict[genre]
    del new_genre_dict['unknown']

    movies_genre_serie = pd.Series(new_genre_dict)   
    # create plot
    movies_genre_serie.plot.pie()

    plt.rcParams.update({"font.size": 12})
    plt.ylabel("")
    plt.title("Movie Genres")

    fig = matplotlib.pyplot.gcf()
    fig.set_size_inches(15, 8.5)
    fig.savefig('images/plot/movie_genres.png')
    plt.clf()



def circular_plot_origin(movies):
    # create serie to plot
    movies_origin = movies["Origin/Ethnicity"].groupby(movies["Origin/Ethnicity"]).count()
    # print(movies_origin)
    origin_dict = {}
    for (origins, num_movies) in movies_origin.items():
        origins_list = origins.split(", ")
        for genre in origins_list:
            if genre in origin_dict:
                origin_dict[genre] += num_movies
            else:
                origin_dict[genre] = num_movies

    new_origin_dict = {}
    new_origin_dict["Others"] = 0
    for genre in list(origin_dict):
        if origin_dict[genre] < 1000:
            new_origin_dict["Others"] += origin_dict[genre]
            origin_dict.pop(genre, None)
        else:
            new_origin_dict[genre] = origin_dict[genre]

    origin_dict = new_origin_dict
    movies_genre_serie = pd.Series(origin_dict)

    # create plot
    movies_genre_serie.plot.pie()

    plt.rcParams.update({"font.size": 12})
    plt.ylabel("")
    plt.title("Movie Origins")

    fig = matplotlib.pyplot.gcf()
    fig.set_size_inches(15, 8.5)
    fig.savefig('images/plot/movie_origins.png')
    plt.clf()


def keywords(movies):
    movies_plots = movies['Plot']
    split = []
    for i in movies_plots:
        word = i.split()
        for j in word:
            if (len(j)>5):
                split.append(j)
      
    # Pass the split_it list to instance of Counter class.
    counter = Counter(split)
    # most_common() produces k frequently encountered
    # input values and their respective counts.
    most_occur = counter.most_common(10)
    print(most_occur)

    

if __name__ == '__main__':
    movies = pd.read_csv("data/wiki_movie_plots_deduped.csv")
    movies = prepare_data(movies)
    plot_movies_decade(movies)
    circular_plot_genre(movies)
    circular_plot_origin(movies)
    keywords(movies)
