import pandas as pd
import random
# do not use seed, this makes random deterministic which we don't want
# random.seed(0)

xls = pd.ExcelFile('imdb.xlsx')
df = xls.parse('imdb')
df_directors = xls.parse('directors')
df_countries = xls.parse('countries')

df["movie_title"] = df["movie_title"].str.replace("Ê", "")
# df["movie_title"] = df["movie_title"].str.replace("Ê", "")

""" Q4:
Who is the director with the most movies? First get the number of movies per "director_name", then save the director's name
and count as a series of length 1 called "director_with_most"
"""

"""# your code here
item = df["director_name"] == "Christopher Nolan"
item2 = df[item]
count = df[item]["director_name"].count()

Q5:
Save all of this director's movies and their ratings in a variable called all_movies_ratings, then print this variable.
(The director with the most movies you got from the last question.)


# your code here
first = df["movie_title"]
second = df["imdb_score"]
print(second)
all_movies_ratings"""

# The part i commented above also doesnt work so I want to have a look as to why

# first we need a list of all the movies with a score over 8.3
# then we need a random number between 0 and the length of the list
# then pick the movie at that index

minimum_score = 8.3

good_movies = df[df["imdb_score"] > minimum_score]

random_movie_index = random.randint(0, len(good_movies) - 1)

movie = good_movies.iloc[random_movie_index]

print(movie)

# rating = df["imdb_score"] > 8.3
# good_movie = df[rating]
# rand_int = random.randint(0, len(good_movie) - 1)
# rand_title = good_movie[rand_int: rand_int + 1]
# rand_title

# Why is it giving me the same number repetedly?
