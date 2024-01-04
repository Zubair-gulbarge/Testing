# Problem: Working with Files (CSV)
# Description: Read and write CSV files using the built-in csv module.
# Code:

import csv

# Write data to a CSV file
with open('example.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Name', 'Age'])
    csvwriter.writerow(['John Doe', 25])
    csvwriter.writerow(['Jane Smith', 30])

# Read data from the CSV file
with open('example.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        print(row)
