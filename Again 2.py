import random
random.seed(0)

# your code here
rating = df["imdb_score"] > 8.3
good_movie = df[rating]
rand_int = randint(0, len(good_movie) - 1)
rand_title = good_movie[rand_int : rand_int + 1]
rand_title

#Why is it giving me the same number repetedly?