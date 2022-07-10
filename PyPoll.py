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


# ________ Import and Open File Object ________
# 1. Import the csv and os modules.
# 2. Add the filename variable that references the path to election_results.csv.
# 3. Open the election_results.csv using the with statement as the filename object, election_data.
# 4. Print the filename object.

# import csv
# import os

# # Assign a variable for the file to load and the path.
# file_to_load = os.path.join("Resources", "election_results.csv")
# # Open the election results and read the file.
# with open(file_to_load) as election_data:

#     # Print the file object.
#      print(election_data)



# _______ Start of Section 3.4.3 _______

# --- Step 1 ---
# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")
# # Using the open() function with the "w" mode we will write data to the file.
# open(file_to_save, "w")


# --- Step 2 ---
# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Use the open statement to open the file as a text file.
# outfile = open(file_to_save, "w")
# # Write some data to the file.
# outfile.write("Hello World")

# # Close the file
# outfile.close()

# --- Step 3 ---
# Clean the Code

# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Using the with statement open the file as a text file.
# with open(file_to_save, "w") as txt_file:

#     # Write some data to the file.
#     txt_file.write("Hello World\nHola Mundo\nGuten Tag Werld\n")


# --- Step 4 ---
# Add data to file

# import csv
# import os

# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Using the with statement open the file as a text file.
# with open(file_to_save, "w") as txt_file:

#     # # Write three counties to the file.
#     # txt_file.write("Arapahoe, ")
#     # txt_file.write("Denver, ")
#     # txt_file.write("Jefferson, ")

#     # ^ OR below outputs the same

#     # # Write three counties to the file.
#     # txt_file.write("Arapahoe, Denver, Jefferson")

#     # Adding the counties on separate lines
#     txt_file.write("Counties in the Election\n" + "-"*25 + "\n" + "Arapahoe\nDenver\nJefferson")


# _______ Start of Section 3.4.4 _______
# --- Step 1 ---
# Read election data 

# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # # Print each row in the CSV file.
    # for row in file_reader:
    #     print(row)

# --- Step 1.1 (exercise) ---
    # # Retrieve the first item from each row
    # for row in file_reader:
    #     print(row[0])
    
    # Print the header row.
    headers = next(file_reader)
    print(headers)


