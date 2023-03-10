# -Add our dependencies.
import csv
import os

# -Assign a variable to load a file from a path.
file_to_load = os.path.join("/Users/kimberlywoods/School-UCSD-DS-Bootcamp/Election_Analysis/Resources/election_results.csv")

# -Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# -Initialize a total vote counter.
total_votes = 0

# -Candidate Options and cadidate votes
candidate_options = []

# -Declare the empty dictionary.
candidate_votes = {}

# -Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# -Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    # -Read the header row.
    headers = next(file_reader)
    #print (headers)

# -Print each row in the CSV file.
    for row in file_reader:
        # -Add to the total vote count.
        total_votes += 1
        
        # -Get the candidate name from each row.
        candidate_name = row[2]

        # -If the candidate does not match any existing candidate add it the candidate list.
        if candidate_name not in candidate_options:
            
            # -Add it to the list of candidates.
            candidate_options.append(candidate_name)
            
            # -Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # -Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-----------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-----------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)


# -Print the candidate vote dictionary and total # of votes
#print (candidate_votes)
#print (total_votes)

# -Determine the percentage of votes for each candidate by looping through the counts.
    for candidate_name in candidate_votes:
        # -Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # -Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100

        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # -Print the candidate name and percentage of votes to the terminal.
        #print(f"{candidate_name}: received {vote_percentage:.2f}% of the vote.")

        # -Print out each candidate's name, vote count, and percentage of votes to the terminal.
        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # -Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)

        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)


        # -Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
             # -Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

    # -Print out the winning candidate, vote count and percentage to terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

#with open(file_to_save, "w") as txt_file:
#    txt_file.write("Election Results\n-------------\n-------------\n")
#    txt_file.write(f"Total Votes: {total_votes}")
#    txt_file.write("Counties in the Election:\n-------------\nArapahoe\nDenver\nJefferson\n")
#    txt_file.write("\nCandidates in the Election:\n---------\n")
#    txt_file.write("Diana DeGette\nCharles Casper Stockham\nRaymon Anthony Doane\n")
#    txt_file.write("\nWinning Candidate Summary:\n")
#    txt_file.write(winning_candidate_summary)

    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)    

# Close the file.
election_data.close()


#Write down the names of all the candidates. -done
#Add a vote count for each candidate. - done
#Get the total votes for each candidate. -done
#Get the total votes cast for the election -done 
