# Dependencies: Importing necessary modules
import os
import csv

# File Path: Defining the path to the budget data CSV file
current_working_dir = os.getcwd()
budget_data_path = os.path.join(current_working_dir, 'Resources', 'budget_data.csv')

# Read CSV: Opening and reading the budget data CSV file
with open(budget_data_path, newline="") as budget_data:
    csvreader = csv.reader(budget_data, delimiter=',')
    csv_header = next(csvreader)

# Lists for Data Storage: Creating lists to store months and profit/loss data
    months = []
    profit_losses = []

# Loop through CSV Data: Reading each row to extract and process data
    for row in csvreader:
        months.append(row[0])
        profit_losses.append(int(row[1]))

# Calcualate Total Months
    total_months = len(months)

# Calculate Average Change
    change = []

    for x in range(1,len(profit_losses)):
        change.append(int(profit_losses[x] - int(profit_losses[x-1])))
        average_change = sum(change) / len(change)

# Find Greatest Increase and Decrease in Profits
    greatest_increase = max(change)
    greatest_decrease = min(change)
    max_month = months[change.index(max(change))]
    min_month = months[change.index(min(change))]

# Print Results to Terminal
    print('Financial Analysis')
    print("----------------------------")
    print('Total Months: ' + str(total_months))
    print('Total: ' + '$' + str(sum(profit_losses)))
    print('Average Change: $' + (str(round(average_change,2))))
    print('Greatest Increase in Profits: ' + str(months[change.index(max(change)) + 1]) + " " + '($' + str(greatest_increase) + ')')
    print('Greatest Decrease in Profits: ' + str(months[change.index(min(change)) + 1]) + " " + '($' + str(greatest_decrease) + ')')

# Output to a Text File
file = open('PyBank.txt', 'w')
file.write('Financial Analysis' + "\n")
file.write("----------------------------" + "\n")
file.write('Total Months: ' + str(total_months) + "\n")
file.write('Total: ' + '$' + str(sum(profit_losses)) + "\n")
file.write('Average Change: $' + (str(round(average_change,2))) + "\n")
file.write('Greatest Increase in Profits: ' + str(months[change.index(max(change)) + 1]) + " " + '($' + str(greatest_increase) + ')'+ "\n")
file.write('Greatest Decrease in Profits: ' + str(months[change.index(min(change)) + 1]) + " " + '($' + str(greatest_decrease) + ')'+ "\n")