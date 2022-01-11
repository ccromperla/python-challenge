import os 
import csv

#Path to collect data from Rescources Folder 
py_bank = os.path.join ('Resources', 'budget_data.csv')

#Empty lists to store data in
months = []
profloss = []
profloss_diff = []

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

        #list comprhension turning string into integer, when reading in a file items are considered strings
        profloss = [int (profloss_values) for profloss_values in profloss]
        
        #Sum of the net total amount over the entire period
        total = sum(profloss)
        print("Total: $" + str(total))
        
        #Use list comprehension to iterate through list and calculate change
        profloss_diff = [profloss[i] - profloss[i - 1] for i in range(1, len(profloss))]

        #Use Function to find Average Change, fron an activity 
        def average(numbers):
            length = len(numbers)
            total = 0.0
            for number in numbers:
                total += number
            return total / length

        #Call average function    
        average(profloss_diff)
        print("Average Change: $" + str((round(average(profloss_diff),2))))

        #find greatest increase and decrease by calling min and max
        greatest_increase = max(profloss_diff)
        greatest_decrease = min(profloss_diff)

        #index into profloss_diff to find greatest increase/decrease in the data
        x = profloss_diff.index(greatest_increase)
        y = profloss_diff.index(greatest_decrease)

        #Find the month associtaed with greatest increase and decrease
        #add 1 because the profloss_diff is off by one (doing f-strigns in pypoll)
        print("Greatest Increase In Profits: " + str(months[x+1]) + " ($" + str(greatest_increase) + ")")
        print("Greatest Decrease In Profits: " + str(months[y+1]) + " ($" + str(greatest_decrease) + ")")

#Specifiy path and file to write into
py_bank = os.path.join("Analysis", "bank_analysis.txt")

#open file using write mode
with open(py_bank, "w") as textfile:

        # Initialize csv.writer
        writer = csv.writer(textfile)
        
        #Write each row
        writer.writerow([("Financial Analysis")])
        writer.writerow(["----------------------------"])
        writer.writerow(["Total Months: " + str(total_months)])
        writer.writerow(["Total: $" + str(total)])
        writer.writerow([("Average Change: $" + str((round(average(profloss_diff),2))))])
        writer.writerow([("Greatest Increase In Profits: " + str(months[x+1]) + " ($" + str(greatest_increase) + ")")])
        writer.writerow([("Greatest Decrease In Profits: " + str(months[y+1]) + " ($" + str(greatest_decrease) + ")")])