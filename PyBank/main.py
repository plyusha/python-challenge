import os
import csv

# Path to the 'budget_data.csv' file
budget_dataCSV = os.path.join("..", "budget_data.csv")

# Defining variables

profit = 0
month_list = []
month_count = 0
total_net = 0
tot_profit = []
avg_change = 0
tot_change = 0
max_change = ['', 0]
min_change = ['', 0]

# Open and read the csv file
with open(budget_dataCSV, newline = '') as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ',')
        
        # Skiping the header
        next(csvreader, None)
        
        # The total number of months included in the dataset equals count of rows of data minus 1 (the header)
        month_count = ((len(open(budget_dataCSV).readlines()))-1)
        
        # Looping through each row of data
        for row in csvreader:
            month = row[0]
            profit = float(row[1])
            month_list.append(month)
            tot_profit.append(profit)
            # The total net amount of "Profit/Losses" over the entire period 
            total_net = sum(tot_profit)
            
        # The total number of months included in the dataset equals count of rows of data minus 1 (the header)
        month_count = ((len(open(budget_dataCSV).readlines()))-1)
            
# Looping to calculate the average change in "Profit/Losses" between months over the entire period
for i in range(1, month_count):
    avg_change = tot_profit[i] - tot_profit[i-1]
    tot_change += avg_change
    if avg_change > max_change[1]:
        max_change = [month_list[i], avg_change]
    if avg_change < min_change[1]:
        min_change = [month_list[i], avg_change]
final_avg_change = tot_change /month_count
        
# Creating text file output
line_1 = 'Financial Analysis'
line_2 = "-"*28
line_3 = "Total Months: " + str(month_count)
line_4 = "Total: " + str(total_net)
line_5 = "Average Change: " + str(final_avg_change)   
line_6 = "Greatest Increase in Profits: " + max_change[0] + ' ($' + str(round(max_change[1])) + ')'       
line_7 = "Greatest Deccrease in Profits: " + min_change[0] + ' ($' + str(round(min_change[1])) + ')'          
summary = []
summary.extend([line_1, line_2, line_3, line_4, line_5, line_6, line_7])

# Report summary data in terminal
print(summary)

# Write summary data into a text file
with open("Output.txt", "w") as text_file:
    print(f"{summary}", file=text_file)
