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

# # Add our dependencies.
# import csv
# import os

# # Assign a variable to load a file from a path.
# file_to_load = os.path.join("Resources", "election_results.csv")

# # Assign a variable to save the file to a path.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Open the election results and read the file.
# with open(file_to_load) as election_data:

#     # Read the file object with the reader function.
#     file_reader = csv.reader(election_data)

#     # # Print each row in the CSV file.
#     # for row in file_reader:
#     #     print(row)

# # --- Step 1.1 (exercise) ---
#     # # Retrieve the first item from each row
#     # for row in file_reader:
#     #     print(row[0])
    
#     # Print the header row.
#     headers = next(file_reader)
#     print(headers)



# # _______ Start of Section 3.5.1 _______
# # --- Step 1 ---
# # 
# # Add our dependencies.
# import csv
# import os
# # Assign a variable to load a file from a path.
# file_to_load = os.path.join("Resources", "election_results.csv")
# # Assign a variable to save the file to a path.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # 1. Initializing the vote counter:
# total_votes = 0

# # Open the election results and read the file.
# with open(file_to_load) as election_data:
#     file_reader = csv.reader(election_data)

#     # Read the header row.
#     headers = next(file_reader)

#     # Print each row in the CSV file.
#     for row in file_reader:
#         # print(row)
#         # 2. Add the total vote count
#         total_votes += 1

# # 3. Print the total 
# print(total_votes)

# # 3.1 optionally add a comma 
# print(f"{total_votes:,}")



# _______ Start of Section 3.5.2 _______
# --- Step 1 ---

# # Add our dependencies.
# import csv
# import os

# # Assign a variable to load a file from a path.
# file_to_load = os.path.join("Resources", "election_results.csv")

# # Assign a variable to save the file to a path.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Initialize a total vote counter.
# total_votes = 0

# # # --- NEW* ---
# # 1. Candidate Options
# candidate_options = []

# # Open the election results and read the file.
# with open(file_to_load) as election_data:
#     file_reader = csv.reader(election_data)

#     # Read the header row.
#     headers = next(file_reader)

#     # Print each row in the CSV file.
#     for row in file_reader:
#         # Add to the total vote count.
#         total_votes += 1

#         # 2. Print the candidate name from each row.
#         candidate_name = row[2]
        
#         # # 3. Add the candidate name to the candidate list.
#         # candidate_options.append(candidate_name)

#         # 4. Inserting an 'if' loop to only add candidate names not already on the list
#         if candidate_name not in candidate_options:

#             # 5. Add the candidate name to the candidate list.
#             candidate_options.append(candidate_name)


# # Print the candidate list.
# print(candidate_options)




# _______ Start of Section 3.5.3 _______

# # Add our dependencies.
# import csv
# import os

# # Assign a variable to load a file from a path.
# file_to_load = os.path.join("Resources", "election_results.csv")

# # Assign a variable to save the file to a path.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Initialize a total vote counter.
# total_votes = 0

# # Candidate options and candidate votes
# candidate_options = []

# # --- NEW* ---
# # 1. Declare the empty dictionary.
# candidate_votes = {}

# # Open the election results and read the file.
# with open(file_to_load) as election_data:
#     file_reader = csv.reader(election_data)

#     # Read the header row.
#     headers = next(file_reader)

#     # Print each row in the CSV file.
#     for row in file_reader:
#         # Add to the total vote count.
#         total_votes += 1

#         # Print the candidate name from each row.
#         candidate_name = row[2]
                        
#         # Inserting an 'if' loop to only add candidate names not already on the list
#         if candidate_name not in candidate_options:

#             # Add the candidate name to the candidate list.
#             candidate_options.append(candidate_name)

#             # 2. Begin tracking that candidate's vote count.
#             candidate_votes[candidate_name] = 0

#             # # 3. Add a vote to that candidate's count. 
#             # --> only adds one vote becuase it's nested in 'if' statement
#             # candidate_votes[candidate_name] += 1

#         # 4. Add a vote to that candidate's count.
#         candidate_votes[candidate_name] += 1


# # Print the candidate vote dictionary.
# print(candidate_votes)

# *** OUTPUT ***



# _______ Start of Section 3.5.4 _______
# To retrieve the votes for each candidate and get the percentage of votes, follow these steps:
# 1. Use a for loop to iterate through the candidate_options = [] list. We will get the candidate's name.
# 2. Use the for loop variable to retrieve the votes of the candidate from the candidate_votes = {} dictionary.
# 3. Calculate the percentage of the vote count.
# 4. Print each candidate and the percentage of votes using f-string formatting.

# # Add our dependencies.
# import csv
# import os

# # Assign a variable to load a file from a path.
# file_to_load = os.path.join("Resources", "election_results.csv")

# # Assign a variable to save the file to a path.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Initialize a total vote counter.
# total_votes = 0

# # Candidate options and candidate votes
# candidate_options = []

# # --- NEW* ---
# # 1. Declare the empty dictionary.
# candidate_votes = {}

# # Open the election results and read the file.
# with open(file_to_load) as election_data:
#     file_reader = csv.reader(election_data)

#     # Read the header row.
#     headers = next(file_reader)

#     # Print each row in the CSV file.
#     for row in file_reader:
#         # Add to the total vote count.
#         total_votes += 1

#         # Print the candidate name from each row.
#         candidate_name = row[2]
                        
#         # Inserting an 'if' loop to only add candidate names not already on the list
#         if candidate_name not in candidate_options:

#             # Add the candidate name to the candidate list.
#             candidate_options.append(candidate_name)

#             # 2. Begin tracking that candidate's vote count.
#             candidate_votes[candidate_name] = 0

#             # # 3. Add a vote to that candidate's count. 
#             # --> only adds one vote becuase it's nested in 'if' statement
#             # candidate_votes[candidate_name] += 1

#         # 4. Add a vote to that candidate's count.
#         candidate_votes[candidate_name] += 1

# # Determine the percentage of votes for each candidate by looping through the counts.
# # 1. Iterate through the candidate list.
# for candidate_name in candidate_votes:
#     # 2. Retrieve vote count of a candidate.
#     votes = candidate_votes[candidate_name]
#     # 3. Calculate the percentage of votes.
#     vote_percentage = float(votes) / float(total_votes) * 100
#     # # 4. Print the candidate name and percentage of votes.
#     # print(f"{candidate_name}: received {vote_percentage}% of the vote.")

#     # 5 Format percentage to 1 decimal place
#     print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")

# # OUTPUT:
# # Charles Casper Stockham: received 23.04854332167558% of the vote.
# # Diana DeGette: received 73.81224794501652% of the vote.
# # Raymon Anthony Doane: received 3.1392087333079077% of the vote.
# #
# # --After formatting:
# # Charles Casper Stockham: received 23.0% of the vote.
# # Diana DeGette: received 73.8% of the vote.
# # Raymon Anthony Doane: received 3.1% of the vote. 





# _______ Start of Section 3.5.4 _______
# The final task is to determine the winning candidate by the number and percentage of votes.
# When we loop through the vote counts, we can:
# - Use an if statement to check if the first vote count for a candidate is greater than zero.
# - If the statement is true, then that vote count will be equal to the "winning count."
# - At the same time, we can set that candidate's percentage of the vote equal to the "winning percentage."
# - Then we can select the candidate as the "winning candidate" from the candidate_options list.

# To do all of this, we will first need to:
# 1. Declare a variable that holds an empty string value for the winning candidate.
# 2. Declare a variable for the "winning count" equal to zero.
# 3. Declare a variable for the "winning_percentage" equal to zero.


# # Add our dependencies.
# import csv
# import os

# # Assign a variable to load a file from a path.
# file_to_load = os.path.join("Resources", "election_results.csv")

# # Assign a variable to save the file to a path.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Initialize a total vote counter.
# total_votes = 0

# # Candidate options and candidate votes
# candidate_options = []

# # Declare the empty dictionary.
# candidate_votes = {}

# # *** NEW ***
# # 1. Winning Candidate and Winning Count Tracker
# winning_candidate = ""
# winning_count = 0
# winning_percentage = 0

# # Open the election results and read the file.
# with open(file_to_load) as election_data:
#     file_reader = csv.reader(election_data)

#     # Read the header row.
#     headers = next(file_reader)

#     # Print each row in the CSV file.
#     for row in file_reader:
#         # Add to the total vote count.
#         total_votes += 1

#         # Print the candidate name from each row.
#         candidate_name = row[2]
                        
#         # Inserting an 'if' loop to only add candidate names not already on the list
#         if candidate_name not in candidate_options:

#             # Add the candidate name to the candidate list.
#             candidate_options.append(candidate_name)

#             # Begin tracking that candidate's vote count.
#             candidate_votes[candidate_name] = 0
            
#         # 4. Add a vote to that candidate's count.
#         candidate_votes[candidate_name] += 1

# # Determine the percentage of votes for each candidate by looping through the counts.
# # Iterate through the candidate list.
# for candidate_name in candidate_votes:
#     # Retrieve vote count of a candidate.
#     votes = candidate_votes[candidate_name]
#     # Calculate the percentage of votes.
#     vote_percentage = float(votes) / float(total_votes) * 100

#     #  Print each candidate's name, vote count, and percentage of
#     # votes to the terminal.
#     print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
#         # OUTPUT
#         # Charles Casper Stockham: 23.0% (85,213)
#         # Diana DeGette: 73.8% (272,892)
#         # Raymon Anthony Doane: 3.1% (11,606) 

#     # Determine winning vote count and candidate
#     # Determine if the votes is greater than the winning count.
#     if (votes > winning_count) and (vote_percentage > winning_percentage):
#          # If true then set winning_count = votes and winning_percent =
#          # vote_percentage.
#          winning_count = votes
#          winning_percentage = vote_percentage
#          # And, set the winning_candidate equal to the candidate's name.
#          winning_candidate = candidate_name

# # Print the winning candidates' results to the terminal.
# winning_candidate_summary = (
#     f"-------------------------\n"
#     f"Winner: {winning_candidate}\n"
#     f"Winning Vote Count: {winning_count:,}\n"
#     f"Winning Percentage: {winning_percentage:.1f}%\n"
#     f"-------------------------\n")

# print(winning_candidate_summary)

#     # OUTPUT
#     #  -------------------------
#     # Winner: Diana DeGette
#     # Winning Vote Count: 272,892
#     # Winning Percentage: 73.8%
#     # -------------------------




# _______ Start of Section 3.6.1 _______


# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate options and candidate votes
candidate_options = []
# Declare the empty dictionary.
candidate_votes = {}

# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]
                        
        # If the candidate does not match any existing candidate add it the
        # the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
           
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # *** NEW ***
    # 1. After opening the file print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")

    # 2. Delete two lines below
    # # Determine the percentage of votes for each candidate by looping through the counts.
    # # Iterate through the candidate list.
    
    # 3. Add two lines below
    # After printing the final vote count to the terminal save the final vote count to the text file.
    txt_file.write(election_results)

    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100

        # 4. Add new variable to add to results
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)

        #  5. Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and 
            # winning_percent = # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

    # Print the winning candidates' results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

    # 6. Re-add this print to terminal
    print(winning_candidate_summary)

    # 7. Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)


# 8. Comment out all below 
    # # Print the final vote count to the terminal.
    # election_results = (
    #     f"\nElection Results\n"
    #     f"-------------------------\n"
    #     f"Total Votes: {total_votes:,}\n"
    #     f"-------------------------\n")
        
    # print(election_results, end="")
    # # Save the final vote count to the text file.
    # txt_file.write(election_results)

