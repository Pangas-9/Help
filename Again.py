# your code here
import csv

sightings_us = []
filepath = "ufo-sightings.csv"

with open(filepath, "r") as csvfile:

    reader = csv.DictReader(csvfile)

    sightings_us = [row for row in reader if row["country"] == "us"]

# First, define a Python function that checks if a given duration (seconds) is "valid"


def is_valid_duration(duration_as_string):
    # your code here

    try:
        duration = float(duration_as_string)

    except ValueError:
        return False

    else:
        return True


# is_valid_duration(sightings_us["duration (seconds)"])


fball = []

for row in sightings_us:

    if row["shape"] == "fireball":

        duration = row["duration (seconds)"]

        if is_valid_duration(duration):

            if float(duration) > 10:

                fball.append(row)

print(fball)
