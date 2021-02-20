#import os
import os
#import csv
import csv

#join correct path
budget_csv = os.path.join("Resources", "budget_data.csv")

#Assignment
#DONE* The total number of months included in the dataset
#DONE* The net total amount of "Profit/Losses" over the entire period
#DONE* Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
#* The greatest increase in profits (date and amount) over the entire period
#* The greatest decrease in losses (date and amount) over the entire period

#Lists to store data
totMonth = [] #finding total number of months
netTot = [] #finding net total
changes = [] #finding changes
maxProf = []
#dates = []
minProf = []

with open(budget_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    
    number = 0 
    nxt_number = 0
    diff_in = 0
    aveChange = 0 
    row_amount = 0
    netTot = 0

    csv_header = next(csvfile)
    
    totMonth = list(csvfile)
    overall_month = len(totMonth)
    ave_overall_month = ((overall_month)-1)

    print(f" ")
    print(f"Financial Analysis")
    print(f"------------------")
    print(f"Total Months: {overall_month}")

#find the total and average
with open(budget_csv) as csvfile:
    csv_reader = csv.reader(csvfile)
    csv_header = next(csvfile)
    for row in csv_reader:

        maxProf.append (float(row[1]))
        #dates.append(str(row[0]))
        minProf.append (float(row[1]))
        row_amount = row_amount + int(row[1])
        if number == 0:
            number = int(row[1])
        else:
            nxt_number = int(row[1])
            diff_in = (nxt_number-number)
            nxt_number = number
    print("Total: " + "$" + str(row_amount))
    aveChange = round((diff_in)/(ave_overall_month),2)
    print("Average Change: " + "$" + str(aveChange))


 
print(f" ")
    