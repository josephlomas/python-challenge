# Importing necessary depencies
import os
import csv

# Set the file path for loading the election data
current_directory = os.getcwd()
election_data_path = os.path.join(current_directory, 'Resources', 'election_data.csv')

# Initialize variables for vote counting candidate tracking
total_votes = 0
candidate_list = []
candidate_votes = {}
candidate_results = ""
winner = ""
win_count = 0
win_percent = 0

# Open and read CSV data to calculate total votes and votes per candidate
with open(election_data_path, newline="") as election_data:
    csvreader = csv.reader(election_data, delimiter=',')
    csv_header = next(csvreader)

# Iterate through each row in the CSV data
    for row in csvreader:
        total_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

# Calculate the percentage of votes each candidate received
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results += f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n"

# Determine the winner based on popular vote count
        if candidate_votes[candidate_name] > win_count:
            winner = candidate_name
            win_count = candidate_votes[candidate_name]

# Print election results to the terminal
print('Election Results')
print("-------------------------")
print('Total Votes:'+ str(total_votes))
print("-------------------------")
print(candidate_results)
print("-------------------------")
print(f"Winner: " + winner)
print("-------------------------")

# Output results to a text file
file = open('PyPoll.txt', 'w')
file.write('Election Results' + "\n")
file.write("-------------------------" + "\n")
file.write('Total Votes:'+ str(total_votes) + "\n")
file.write("-------------------------" + "\n")
file.write(candidate_results + "\n")
file.write("-------------------------" + "\n")
file.write(f"Winner: " + winner + "\n")
file.write("-------------------------" + "\n")