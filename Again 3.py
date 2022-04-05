
import pandas as pd

xls = pd.ExcelFile('imdb.xlsx')
df = xls.parse('imdb')
df_directors = xls.parse('directors')
df_countries = xls.parse('countries')
df["movie_title"] = df["movie_title"].str.replace("Ê", "")

df = pd.merge(left= df, right= df_countries, how= "inner", left_on= "country_id", right_on='id')
df = pd.merge(left= df, right= df_directors, how= "inner", left_on= "director_id", right_on='id')


""" Q4:
Who is the director with the most movies? First get the number of movies per "director_name", then save the director's name
and count as a series of length 1 called "director_with_most"
"""

# your code here
item = df["director_name"] == "Christopher Nolan"
item2 = df[item]
count = df[item]["director_name"].count()


"""Q5:
Save all of this director's movies and their ratings in a variable called all_movies_ratings, then print this variable.
(The director with the most movies you got from the last question.)
"""

# your code here
first = df["movie_title"]
second = df["imdb_score"]
print(second)
all_movies_ratings
