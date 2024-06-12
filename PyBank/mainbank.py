#PyBank
import os
import csv

#path to data in resource folder
pybank_csv = os.path.join('.', 'Resources', 'budget_data.csv')

#Reading using CSV module
with open(pybank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        print(row)

