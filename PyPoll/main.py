import os 
import csv

#Path to collect data from Resources folder
py_poll = os.path.join ('Resources', 'election_data.csv')

#Empty lists to store data
voter_id = []
county = []
canidate = []

#Read in the csv file
with open(py_poll) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')

        #Skip and store header
        header = next(csvreader)
        
        #Loop through and store columns of data into empty lists
        for row in csvreader:
            voter_id.append(row[0])
            county.append(row[1])
            canidate.append(row[2])

        #Find total number of votes by using len
        total_votes = len(voter_id)

        #List of all canidates who received Votes
        canidate_list = ["Khan", "Correy", "Li", "O'Tooley"]

        #Set counter to zero
        khan_votes = 0
        correy_votes = 0
        li_votes = 0
        otooley_votes = 0

        #Loop thru each canidate and add to their counter if they recevied a vote
        for i in range(0,len(canidate)):
            if canidate [i] == "Khan":
                khan_votes += 1
            elif canidate [i] == "Correy":
                correy_votes += 1
            elif canidate [i] == "Li":
                li_votes += 1
            else:
                canidate [i] == "O'Tooley"
                otooley_votes += 1
        
        #Calculate the percent
        khan_percent = (khan_votes/total_votes) * 100
        correy_percent = (correy_votes/total_votes) * 100
        li_percent = (li_votes/total_votes) * 100
        otooley_percent = (otooley_votes/total_votes) * 100

        #Determine the winner by calling max function, by using canidate's count to detemine which canidate from canidate list had max vote
        winner = max(canidate_list, key = canidate.count)

        #print out the election result 
        #percentage is formatted to a string to three decimal places
        print('Election Results')
        print('-------------------------')
        print(f'Total Votes: {len(voter_id)}')
        print('------------------------')
        print(f"{canidate_list[0]}: {khan_percent:.3f}% ({khan_votes})")
        print(f"{canidate_list[1]}: {correy_percent:.3f}% ({correy_votes})")
        print(f"{canidate_list[2]}: {li_percent:.3f}% ({li_votes})")
        print(f"{canidate_list[3]}: {otooley_percent:.3f}% ({otooley_votes})")
        print('-------------------------')
        print(f"Winner: {winner}")

py_poll = os.path.join("Analysis", "election_results.txt")

with open(py_poll, "w") as datafile:
        writer = csv.writer(datafile)

        writer.writerow(['Election Results'])
        writer.writerow(['----------------------------'])
        writer.writerow([(f'Total Votes: {len(voter_id)}')])
        writer.writerow([('------------------------')])
        writer.writerow([(f"{canidate_list[0]}: {khan_percent:.3f}% ({khan_votes})")])
        writer.writerow([(f"{canidate_list[1]}: {correy_percent:.3f}% ({correy_votes})")])
        writer.writerow([(f"{canidate_list[2]}: {li_percent:.3f}% ({li_votes})")])
        writer.writerow([(f"{canidate_list[3]}: {otooley_percent:.3f}% ({otooley_votes})")])
        writer.writerow(['-------------------------'])
        writer.writerow([(f"Winner: {winner}")])  