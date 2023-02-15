# The data I need to retrive.
#Resources/election_results.csv
#/Users/kimberlywoods/School-UCSD-DS-Bootcamp/Election_Analysis/Resources

import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("/Users/kimberlywoods/School-UCSD-DS-Bootcamp/Election_Analysis/Resources/election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("/Users/kimberlywoods/School-UCSD-DS-Bootcamp/Election_Analysis/analysis")

# 1. Initialize a total vote counter.
total_votes = 0

# Candidate Options
candidate_options = []

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    

    # Read the header row.
    headers = next(file_reader)

# Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1
        
# Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

# Print the candidate list.
print(candidate_options)


# To do: perform analysis.
#  print(election_data)

# Close the file.
#election_data.close()


#Write down the names of all the candidates.
#Add a vote count for each candidate.
#Get the total votes for each candidate.
#Get the total votes cast for the election
