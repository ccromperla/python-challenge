import os 
import csv

py_poll = os.path.join ('Resources', 'election_data.csv')

voter_id = []
county = []
canidate = []

with open(py_poll) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')

        header = next(csvreader)

        print("Election Results")
        print(" -------------------------")

        for row in csvreader:
            voter_id.append(row[0])
            county.append(row[1])
            canidate.append(row[2])

        total_votes = len(voter_id)
        print("Total Votes: " + str(len(voter_id)))

        canidate_set = sorted(set(canidate))
        canidate_list = list(canidate_set)

        khan_votes = 0
        correy_votes = 0
        li_votes = 0
        otooley_votes = 0

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
        
        khan_percent = (khan_votes/total_votes) * 100
        correy_percent = (correy_votes/total_votes) * 100
        li_percent = (li_votes/total_votes) * 100
        otooley_percent = (otooley_votes/total_votes) * 100

        winner = max(canidate_list, key = canidate.count)

        print('Election Results')
        print('-------------------------')
        print("Total Votes: " + str(len(voter_id)))
        print('------------------------')
        print(f"{canidate_list[1]}: {khan_percent: .3f}% ({khan_votes})")
        print(f"{canidate_list[0]}: {correy_percent: .3f}% ({correy_votes})")
        print(f"{canidate_list[2]}: {li_percent: .3f}% ({li_votes})")
        print(f"{canidate_list[3]}: {otooley_percent: .3f}% ({otooley_votes})")
        print('-------------------------')
        print(f"Winner: {winner}")


        # ('Election Results')
        # ('-------------------------')
        # ("Total Votes: " + str(len(voter_id)))
        # ('------------------------')
        # (f"{canidate_list[1]}: {khan_percent: .3f}% ({khan_votes})")
        # (f"{canidate_list[0]}: {correy_percent: .3f}% ({correy_votes})")
        # (f"{canidate_list[2]}: {li_percent: .3f}% ({li_votes})")
        # (f"{canidate_list[3]}: {otooley_percent: .3f}% ({otooley_votes})")
        # ('-------------------------')
        # (f"Winner: {winner}")

py_poll = os.path.join("Resources", "election_results.txt")

with open(py_poll, "w") as datafile:
        writer = csv.writer(datafile)

        writer.writerow(['Election Results'])
        writer.writerow(['----------------------------'])
        # writer.writerow(["Total Votes: " + str(len(voter_id))])
        # writer.writerow([f"{canidate_list[1]}: {khan_percent: .3f}% ({khan_votes})")]
        # writer.writerow([f"{canidate_list[0]}: {correy_percent: .3f}% ({correy_votes})"])
        # writer.writerow([f"{canidate_list[2]}: {li_percent: .3f}% ({li_votes})"])
        # writer.writerow([f"{canidate_list[3]}: {otooley_percent: .3f}% ({otooley_votes})"])
        # writer.write.row([f"{canidate_list[3]}: {otooley_percent: .3f}% ({otooley_votes})"])
        # writer.write.row(['-------------------------'])
        # writer.wrtie.row([f"Winner: {winner}"])
                # for canidates in range(1,len(canidate)):
        #     if canidates == "Khan":
        #         print(canidates)

    # def polling_results(polling_data)

    #     voter_id = (polling_data[0])
    #     county = (polling_data[1])
    #     canidate = (polling_data[2])

    #     total_votes = len(voter_id)

    #     print("Total Votes: " + str(len(voter_id))
    