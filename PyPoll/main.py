import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')
outputpath = os.path.join('Analysis','election_analysis.txt')

total_votes = 0
individual_votes = 0
candidates_list = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    print(csvreader)
    header_row = next(csvreader)
    first_data_row = next(csvreader)
    total_votes = 1
    for rows in csvreader:
        total_votes += 1
        voters = rows[0]
        candidate = str(rows[2])
        if candidate not in candidates_list:
            candidates_list.append(candidate)
        

    print(total_votes)    
    print(candidates_list)



output = (f'Election Results\n'
f'-------------------------\n'
f'Total Votes: {total_votes}\n'
f'-------------------------\n'
f'print(candidates_list[0]): 23.049% (85213)\n'
f'print(candidates_list[1]): 73.812% (272892)\n'
f'print(candidates_list[2]): 3.139% (11606)\n'
f'-------------------------\n'
f'Winner: Diana DeGette\n'
f'-------------------------')

# print(output)
# with open(outputpath, 'w') as f:
#     f.write(output)