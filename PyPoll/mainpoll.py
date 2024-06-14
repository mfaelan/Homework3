#PyPoll

import os
import csv

#path to data in resource folder
pypoll_csv = os.path.join('.', 'Resources', 'election_data.csv')

with open(pypoll_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    # skip header row
    print(f"Header: {csv_header}")

count = 0
candidatelist = []
unique_candidate = []
vote_count = []
vote_percent = []

# Open the CSV using the set path PyPollcsv

with open(pypoll_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    # Conduct the ask
    for row in csvreader:
        # Count the total number of votes
        count = count + 1
        # Set the candidate names to candidatelist
        candidatelist.append(row[2])
        # Create a set from the candidatelist to get the unique candidate names
    for x in set(candidatelist):
        unique_candidate.append(x)
        # y is the total number of votes per candidate
        y = candidatelist.count(x)
        vote_count.append(y)
        # z is the percent of total votes per candidate
        z = (y/count)*100
        vote_percent.append(z)
        
    winning_vote_count = max(vote_count)
    winner = unique_candidate[vote_count.index(winning_vote_count)]

    
    # print the Results
    print("Election Results")
    print("...................................................................")
    for i in range(len(unique_candidate)):
            print(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i])+ ")")
    print("....................................")
    print("Winner:" + winner )

# output to a text file
    file = open("output.txt","w")
    file.write("Election Results" + "\n")
    file.write(".............................................................." + "\n")
    for i in range(len(unique_candidate)):
            file.write(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i])+ ")" + "\n")
    file.write("Winner:" + winner + "\n")
    file.close()