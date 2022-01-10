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

        #Defining a function in order to find the length of the list
        def bank_month(month_length):
            #Print total months
            print("Total Months: " + str(len(month_length)))
        #Call bank_month function
        bank_month(months)

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
        print(greatest_increase) 
        print(greatest_decrease)

        #print(months)
        #print(profloss_diff)

        #if greatest_increase