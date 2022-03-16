'''
row for row in sightings_us:
            if row["duration (seconds)"] > is_valid_duration and row["shape"] == "fireball":
                fball.append(row)
4. Let's find the "fireball" sighting(s) that lasted more than ten seconds in US. 
Print the the datetime and state of each.  Put the data in "fball" and print the result.

Note: Consider only the US sightings stored in "sightings_us".

- Cast the duration in seconds to a float (decimal). 
- Check if duration is greater than 10. 
- Check if the shape is "fireball".

'''

# First, define a Python function that checks if a given duration (seconds) is "valid"
import csv
filepath = "ufo-sightings.csv"


def is_valid_duration(duration_as_string):
    # your code here
    duration = float(int(duration_as_string))
    sightings_us = []
    fball = []

    csvfile = open(filepath, "r")

    reader = csv.DictReader(csvfile)

    for row in reader:

        shape = row["shape"]

        if shape == "fireball":

            fireballDuration = getFloat(row["duration (seconds)"])

            if fireballDuration > duration:
                fball.append(row)

                # print("fireball", fireballDuration)

    for row in fball:
        print(row["datetime"], row["state"])

    # reader

    # time = float(int(reader["duration (seconds)"]))

    # sightings_us = [row for row in reader if row["country"] == "us"]
    # fball = [
    #     row for row in sightings_us if row["duration (seconds)"] > time and row["shape"] == "fireball"]
    # print(fball)


def getFloat(duration):
    try:
        return float(duration)
    except:
        return float(int(duration))


is_valid_duration("10")
