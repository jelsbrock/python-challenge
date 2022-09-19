import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')
outputpath = os.path.join('Analysis','budget_analysis.txt')

total_months = 0
total_amount = 0
net_pl = 0
net_pl_list = []
gr_increase = 0
gr_decrease = 1000000000

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    print(csvreader)
    header_row = next(csvreader)
    first_data_row = next(csvreader)
    total_months = 1
    total_amount = int(first_data_row[1])
    previous_amount = int(first_data_row[1])
    for rows in csvreader:
        total_months += 1
        total_amount += int(rows[1])
        net_pl = int(rows[1]) - previous_amount
        net_pl_list.append(net_pl)
        previous_amount = int(rows[1])
        if net_pl > gr_increase:
            gr_increase = net_pl
            gr_inc_month = rows[0]
        if net_pl < gr_decrease:
            gr_decrease = net_pl
            gr_dec_month = rows[0]

    output = (f'Financial Analysis\n'
f'----------------------------\n'
f'Total Months: {total_months}\n'
f'Total: ${total_amount}\n'
f'Average Change: ${round(sum(net_pl_list)/(total_months -1), 2)}\n'
f'Greatest Increase in Profits: {gr_inc_month} (${gr_increase})\n'
f'Greatest Decrease in Profits: {gr_dec_month} (${gr_decrease})')

print(output)
with open(outputpath, 'w') as f:
    f.write(output)