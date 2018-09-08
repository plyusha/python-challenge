import os
import csv

# Path to the 'election_data.csv' file
electiondata = os.path.join('Resources', 'election_data.csv')

# Defining variables

candidates = {}
votes_count = 0
votes = 0

# Open and read the csv file
with open(electiondata, newline = '') as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ',')
        
        # Skiping the header
        next(csvreader, None)

#        # The total number of votes cast by counting all of the records in the file excluding the header
#        total_votes = ((len(open(electiondata).readlines()))-1)
        
        # Loop through looking for the data
        for row in csvreader:
            if row[2] not in candidates.keys():
                candidates[row[2]] = 0
            candidates[row[2]] = candidates[row[2]] + 1
            
        # Creating complete list of candidates who received votes by adding unique candidates to the new list
        for votes in candidates.values():
            votes_count = votes_count + votes
        
        
        # Write summary data into a text file
with open("Output.txt", "w") as text_file:
        # Creating text file output
        print("Election Results")
        text_file.write("Election Results")
        line = "-"*25
        print(line)
        text_file.write(line)
        print("Total Votes: " + str(votes_count))
        text_file.write("Total Votes: " + str(votes_count)+ "\n")
        print(line)
        text_file.write(line)
        
        # The percentage of votes each candidate won
        for i, votes in candidates.items():
            percentage = votes/votes_count
            print(i + ": " + '{:.1%}'.format(percentage) + " (" + str(votes) + ")")
            text_file.write(i + ": " + '{:.1%}'.format(percentage) + " (" + str(votes) + ")")
        print(line)
        text_file.write(line)

        # Looping through the candidates to select the winner
        for name in candidates.keys():
            if candidates[name] > votes:
                winner = name
                votes = candidates[name]
        print('Winner: ' + winner)
        text_file.write('Winner: ' + winner)
        print(line)
        text_file.write(line)
        text_file.close()
        
