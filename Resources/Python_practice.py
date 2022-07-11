#print("Hello World!")

#using if statements
#counties = ["Arapahoe","Denver","Jefferson"]
#if counties[1] == 'Denver':
#    print(counties[1])

#example of 'Out of bounds' statement (there is no 4th position)
#if counties[3] != 'Jefferson':
#
#   print(counties[2])

#if-else practice
#temperature = int(input("What is the temperature outside? "))
#
#if temperature > 80:
#    print("Turn on the AC.")
#else:
#    print("Open the windows.")

print("-" * 60)
# 
# Nested If-Else Statements

#What is the score?
#score = int(input("What is your test score? "))

# Determine the grade.
# Step 2: converting to elif statements below
#if score >= 90:
#    print('Your grade is an A.')
#else:
#    if score >= 80:
#        print('Your grade is a B.')
#    else:
#        if score >= 70:
#            print('Your grade is a C.')
#        else:
#            if score >= 60:
#                print('Your grade is a D.')
#            else:
#                print('Your grade is an F.')

# Determine the grade.
#if score >= 90:
#    print('Your grade is an A.')
#elif score >= 80:
#    print('Your grade is a B.')
#elif score >= 70:
#    print('Your grade is a C.')
#elif score >= 60:
#    print('Your grade is a D.')
#else:
#    print('Your grade is an F.')


# Membership Operators
counties = ["Arapahoe","Denver","Jefferson"]
#if "El Paso" in counties:
#    print("El Paso is in the list of counties.")
#else:
#    print("El Paso is not the list of counties.")
#
#print("-" * 20)
#if "Arapahoe" in counties and "El Paso" in counties:
#    print("Arapahoe and El Paso are in the list of counties.")
#else:
#    print("Arapahoe or El Paso is not in the list of counties.")

#print("-" * 20)
#if "Arapahoe" in counties or "El Paso" in counties:
#    print("Arapahoe or El Paso is in the list of counties.")
#else:
#    print("Arapahoe and El Paso are not in the list of counties.")

#print("-" * 20)
#if "Arapahoe" in counties and "El Paso" not in counties:
#   print("Only Arapahoe is in the list of counties.")
#else:
#    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

#print("-" * 40)

#for county in counties:
#    print(county)

#numbers = [0, 1, 2, 3, 4]
#for num in numbers:
#    print(num)
#print("-" * 20)

#for num in range(5):
#    print(num)

#for i in range(len(counties)):
#    print(counties[i])



# ______ Iterate Through Lists and Tuples ______

#counties_tuple = ("Arapahoe","Denver","Jefferson")

#print("-" * 20)
#for i in range(len(counties_tuple)):
#    print(counties_tuple[i])

#print("-" * 20)
#for county in counties_tuple:
#      print(county)

#print("-" * 20)
#for i in len(counties_tuple):
#      print(counties_tuple[i])


# ______ Iterate Through a Dictionary ______
# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# --- Get the Keys of a Dictionary ---
# #for county in counties_dict:
#    print(county)
#print("-" * 20)

#for county in counties_dict.keys():
#    print(county)
#print("-" * 20)


# --- Get the Values of a Dictionary ---
#for county in counties_dict.values():
#    print(county)
#print("-" * 20)

#for county in counties_dict:
#    print(counties_dict[county])
#print("-" * 20)

#for county in counties_dict:
#    print(counties_dict.get(county))
#print("-" * 20)


# --- Get the Key-Value Pairs of a Dictionary ---
#for county, voters in counties_dict.items():
#    print(county, voters)
#print("-" * 20)

#for county, voters in counties_dict.items():
#    print(county, voters)
#    i = county
#    j = voters
#    print(i + " county has " + str(j) + " registered voters")
#    print(county + " county has", str(voters) + " registered voters.")
#    print(county + " county has " + str(voters) + " registered voters.")
#print("-" * 20)


# ______ Iterate Through a List of Dictionaries ______
# print("______ Iterate Through a List of Dictionaries ______")
# print("-" * 40)
# # --- Get Each Dictionary in a List of Dictionaries ---
# voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
#                 {"county":"Denver", "registered_voters": 463353},
#                 {"county":"Jefferson", "registered_voters": 432438}]

# for county_dict in voting_data:
#     print(county_dict)
# print("-" * 20)


# for i in range(len(voting_data)):
#       print(voting_data[i]['county'])


# # --- Get the Values from a List of Dictionaries ---
# print("--- Get the Values from a List of Dictionaries ---")
# for county_dict in voting_data:
#     for value in county_dict.values():
#         print(value)
# print("-" * 20)

# print("-- Retrieve the number of registered voters from each dictionary --")
# for county_dict in voting_data:
#      print(county_dict['registered_voters'])

# print("-- Retrieve the county name from each dictionary --")
# for county_dict in voting_data:
#      print(county_dict['county'])


# ______ F-strings: Formatted String Literals ______
# print("______ F-strings: Formatted String Literals ______")
# print("-" * 40)

#-- Original input --
#my_votes = int(input("How many votes did you get in the election? "))
#total_votes = int(input("What is the total votes in the election? "))
#percentage_votes = (my_votes / total_votes) * 100
#print("I received " + str(percentage_votes)+"% of the total votes.")

#-- f-string literal --
#my_votes = int(input("How many votes did you get in the election? "))
#total_votes = int(input("What is the total votes in the election? "))
#print(f"I received {my_votes / total_votes * 100}% of the total votes.")

#--- Using F-Strings with Dictionaries ---
#print("--- Using F-Strings with Dictionaries ---")
#counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
#for county, voters in counties_dict.items():
#    print(county + " county has " + str(voters) + " registered voters.")

#for county, voters in counties_dict.items():
#    print(f"{county} county has {voters} registered voters.")


#--- Multiline F-Strings ---
#print("--- Multiline F-Strings ---")
#candidate_votes = int(input("How many votes did the candidate get in the election? "))
#total_votes = int(input("What is the total number of votes in the election? "))
#message_to_candidate = (
#    f"You received {candidate_votes} number of votes. "
#    f"The total number of votes in the election was {total_votes}. "
##    f"You received {candidate_votes / total_votes * 100}% of the total votes.")
#    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

#print(message_to_candidate)

#skill Drill_3.2.11
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county, voters in counties_dict.items():
#     print(f"{county} county has {voters} registered voters.")
     print(f"{county} county has {voters} registered voters.")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
for vd in voting_data:
    print(f'{vd["county"]} county has {vd["registered_voters"]:,} registered voters.')
