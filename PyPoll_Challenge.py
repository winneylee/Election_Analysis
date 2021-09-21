# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
counties = []
counties_vote = {}


# Track the winning candidate, vote count and percentage
winning_candidate = ""
candidate_winning_count = 0
candidate_winning_percentage = 0

# 2: Track the largest county and county voter turnout.
largest_counties = ""
counties_turnover = 0
counties_winning_count=0


# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        counties_name = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if counties_name not in counties:

            # 4b: Add the existing county to the list of counties.
            counties.append(counties_name)

            # 4c: Begin tracking the county's vote count.
            counties_vote[counties_name] = 0

        # 5: Add a vote to that county's vote count.
        counties_vote[counties_name] += 1
        

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary.
    for counties_name in counties_vote:

        # 6b: Retrieve the county vote count.
        votes = counties_vote.get(counties_name)

        # 6c: Calculate the percentage of votes for the county.
        votes_percentage = float(votes) / float(total_votes) * 100

         # 6d: Print the county results to the terminal.
        counties_reaults = (
            f"{counties_name}: {votes_percentage:.1f}% ({votes:,})\n")

        print(counties_reaults)
         # 6e: Save the county votes to a text file.
        txt_file.write(counties_reaults)

         # 6f: Write an if statement to determine the winning county and get its vote count.
        if (votes > counties_winning_count):
            counties_winning_count = votes
            counties_turnover= counties_name

    # 7: Print the county with the largest turnout to the terminal.
    winning_counties_summary = (
        f"----------------------\n"
        f"Largest county turnover: {counties_turnover}\n"
        f"-----------------------\n"
    )
    print(winning_counties_summary)

    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(winning_counties_summary)

    # Save the final candidate vote count to the text file.
    

    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > candidate_winning_count):
            candidate_winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {candidate_winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
