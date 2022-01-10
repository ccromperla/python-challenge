import os 
import csv

py_poll = os.path.join ('Resources', 'election_data.csv')

voter_id = []
county = []
canidate = []
khan_votes = []

with open(py_poll) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')

        header = next(csvreader)

        print("Election Results")
        print(" -------------------------")

        for row in csvreader:
            voter_id.append(row[0])
            county.append(row[1])
            canidate.append(row[2])
        
        def poll_votes(total_votes):
            print("Total Votes: " + str(len(total_votes)))
            print(" -------------------------")
        poll_votes(voter_id)

        for canidates in canidate:
            if canidates == Khan:
                khan_votes.append 
                print(len(khan_votes))  
