# -*- coding: UTF-8 -*-
"""PyBank Financial Analysis."""

# Dependencies
import csv
import os

# Files to load and output
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
previous_net = 0
net_change_list = []
month_of_change = []
greatest_increase = ["", 0]  # To store the month and value
greatest_decrease = ["", 999999999999999999]  # To store the month and value

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract the first row to set the initial state for net change calculations
    first_row = next(reader)
    total_months += 1
    total_net += int(first_row[1])
    previous_net = int(first_row[1])

    # Process each row of data
    for row in reader:
        # Track the total number of months
        total_months += 1
        
        # Track the total net amount of "Profit/Losses"
        total_net += int(row[1])

        # Calculate the net change for this month and append to list
        net_change = int(row[1]) - previous_net
        net_change_list.append(net_change)
        month_of_change.append(row[0])
        previous_net = int(row[1])

        # Determine the greatest increase in profits (date and amount)
        if net_change > greatest_increase[1]:
            greatest_increase = [row[0], net_change]

        # Determine the greatest decrease in losses (date and amount)
        if net_change < greatest_decrease[1]:
            greatest_decrease = [row[0], net_change]

# Calculate the average net change across the months
average_change = sum(net_change_list) / len(net_change_list)

# Generate the output summary
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

# Print the output summary to the terminal
print(output)

# Write the output summary to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
