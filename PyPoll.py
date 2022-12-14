# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The winner of the election based on popular vote

# Add our dependencies
import csv
import os
# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources","election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("Analysis","election_analysis.txt")

# Initialize a total vote counter
total_votes = 0

# Declare a new list for candidates
candidate_options = []

# Declare dictionary for votes per candidate
candidate_votes = {}

# Declare Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)
    
    # Print each row in the CSV File
    for row in file_reader:
        # Add the total vote count
        total_votes += 1

        # Print the candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match existing candidate
        if candidate_name not in candidate_options:
            # Add candidate name to candidate options list
            candidate_options.append(candidate_name)

            # Begin tracking candidate's vote count
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# Save the results to our text file
with open(file_to_save, "w") as txt_file:

    # Print the final count to the terminal
    election_results = (
    f"\nElection Results\n"
    f"-----------------------\n"
    f"Total Votes: {total_votes:,}\n"
    f"-----------------------\n")
    #print
    print(election_results, end="")
    #Save the final vote count to the text file
    txt_file.write(election_results)

    # Determine the percentage of votes for each candidate by looping throught the counts
    # Iterate through the candidate list
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes)*100
        
        # Set candidate_results variable
        candidate_results = (f'{candidate_name:} {vote_percentage:.1f}% ({votes:,})\n')

        #P Print each candidate, their vote count, and percentage to the terminal
        print(candidate_results)
        # Save to terminal
        txt_file.write(candidate_results)

        # Determine winning vote count and candidate
        #Determine if the votes are greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):

            # If true then set winning_count = votes and winning_percentage = vote_percentage
            # Vote percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # Set the winning_candidate equal to the candidate's name
            winning_candidate = candidate_name
    
    # Print the winning candidates' results to the terminal
    winning_candidate_summary = (
        f"-----------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-----------------------\n")

    # Print winning candidate's name to the terminal
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
