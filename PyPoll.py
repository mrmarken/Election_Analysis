# The data we need to retrieve:
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

# Import the datetime class from the datetime module.
# (1) import datetime
# (2)
# import datetime as dt

# Use the now() attribute on the datetime class to get the present time.
# (1) now = datetime.datetime.now()
# (2)
# now = dt.datetime.now()

# Print the present time.
# print("The time right now is ", now)


# ________ Read Data from a File ________

# Assign a variable for the file to load and the path.
# file_to_load = 'Resources/election_results.csv'

# __Step1__
# Open the election results and read the file.
# election_data = open(file_to_load, 'r')

# To do: perform analysis.

# Close the file.
# election_data.close()


# __Step2__
# with open(file_to_load) as election_data:
    # To do: perform analysis.
    # print(election_data)


# ________ Import and ________
# 1. Import the csv and os modules.
# 2. Add the filename variable that references the path to election_results.csv.
# 3. Open the election_results.csv using the with statement as the filename object, election_data.
# 4. Print the filename object.

import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
     print(election_data)

