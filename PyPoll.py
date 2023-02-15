# The data I need to retrive.
#Resources/election_results.csv
#/Users/kimberlywoods/School-UCSD-DS-Bootcamp/Election_Analysis/Resources

import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("/Users/kimberlywoods/School-UCSD-DS-Bootcamp/Election_Analysis/Resources/election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    

    # Print the header row.
    headers = next(file_reader)
    print(headers)
def error(i):
    try:
            val = next(i)
            print(val)
    except StopIteration:
            print("Done")
b = value(x)
b = value(a)
error(b)
b
error(b)
error(b)
error(b)
error(b)



# To do: perform analysis.
#  print(election_data)

# Close the file.
#election_data.close()


#Write down the names of all the candidates.
#Add a vote count for each candidate.
#Get the total votes for each candidate.
#Get the total votes cast for the election
