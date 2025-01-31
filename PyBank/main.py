# -*- coding: UTF-8 -*-
"""PyBank Homework Solution."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
net_changes = []
months = []

# Open and read the CSV
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)
    
    # Skip the header row
    header = next(reader)
    
    # Extract first row to initialize net change tracking
    first_row = next(reader)
    total_months += 1
    total_net += int(first_row[1])
    previous_net = int(first_row[1])
    
    # Process each row of data
    for row in reader:
        # Track the month
        month = row[0]
        months.append(month)

        # Track the total net amount
        current_net = int(row[1])
        total_net += current_net

        # Track the monthly net change
        net_change = current_net - previous_net
        net_changes.append(net_change)
        previous_net = current_net

# Calculate the required statistics
average_change = sum(net_changes) / len(net_changes)
greatest_increase = max(net_changes)
greatest_decrease = min(net_changes)
greatest_increase_month = months[net_changes.index(greatest_increase)]
greatest_decrease_month = months[net_changes.index(greatest_decrease)]

# Generate the output summary
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months + len(months)}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n"
)

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)

