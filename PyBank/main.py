import os 
import csv

#Path to collect data from Rescources Folder 
py_bank = os.path.join ('Resources', 'budget_data.csv')

#Empty lists to store data in
months = []
profloss = []

#Read in the csv file
with open(py_bank) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')

        #Skip header
        header = next(csvreader)

        #Store values in list
        for row in csvreader:
            months.append(row[0])
            profloss.append(row[1])

        print("Financial Analysis")
        print("----------------------------")

        #use len to find the total months
        total_months = len(months)
        print("Total Months: " + str(total_months))

        #list comprhension turning string into integer
        profloss = [int (profloss_values) for profloss_values in profloss]
        
        #Sum of the net total amount over the entire period
        total = sum(profloss)
        print("Total: $" + str(total))

        #Determine Change [not yet average] by creating a new list to store this data 
        profloss_diff = []
        
        #Use list comprehension to iterate through list and calculate change
        profloss_diff = [profloss[i] - profloss[i - 1] for i in range(1, len(profloss))]

        #Use Function to find Average Change
        def average(numbers):
            length = len(numbers)
            total = 0.0
            for number in numbers:
                total += number
            return total / length

        #Call average function    
        average(profloss_diff)
        print("Average Change: $" + str((round(average(profloss_diff),2))))

        greatest_increase = max(profloss_diff)
        greatest_decrease = min(profloss_diff)

        x = profloss_diff.index(greatest_increase)
     
        y = profloss_diff.index(greatest_decrease)

        print(f"Greatest Increase In Profits: {months[x+1]} (${greatest_increase})")
        print(f"Greatest Decrease In Profits: {months[y+1]} (${greatest_decrease})")

py_bank = os.path.join("Resources", "bank_analysis.txt")

with open(py_bank, "w") as datafile:
        writer = csv.writer(datafile)

        writer.writerow([("Financial Analysis")])
        writer.writerow(["----------------------------"])
        writer.writerow(["Total Months: " + str(total_months)])
        #writer.writerow([("Total: $" + str(total))]
        writer.writerow([("Average Change: $" + str((round(average(profloss_diff),2))))])
        #writer.writerow([(f"Greatest Increase In Profits: {months[x+1]} (${greatest_increase})")])
        #writer.writerow([(f"Greatest Decrease In Profits: {months[y+1]} (${greatest_decrease})")])