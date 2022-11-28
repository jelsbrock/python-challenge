import os
import csv

csvpath = 'HW\python-challenge\PyPoll\Resources\election_data.csv'
outputpath = 'HW\python-challenge\PyPoll\Analysis\election_analysis.txt'

total_votes = 0
candidate_1_votes = 0
candidate_2_votes = 0
candidate_3_votes = 0
candidates_list = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    print(csvreader)
    header_row = next(csvreader)
    first_data_row = next(csvreader)
    total_votes = 1
    for rows in csvreader:
        total_votes += 1
        candidate = str(rows[2])
        if candidate not in candidates_list:
            candidates_list.append(candidate)
        if candidate == candidates_list[0]:
            candidate_1_votes += 1
        elif candidate == candidates_list[1]:
            candidate_2_votes += 1
        else:
            candidate_3_votes += 1

    if candidate_1_votes > candidate_2_votes and candidate_1_votes > candidate_3_votes:
        winner = candidates_list[0]
    elif candidate_2_votes > candidate_1_votes and candidate_2_votes > candidate_3_votes:
        winner = candidates_list[1]
    else:
        winner = candidates_list[2]

output = (f'Election Results\n'
f'-------------------------\n'
f'Total Votes: {total_votes}\n'
f'-------------------------\n'
f'{candidates_list[0]}: {round(candidate_1_votes * 100/total_votes, 2)}% ({candidate_1_votes})\n'
f'{candidates_list[1]}: {round(candidate_2_votes * 100/total_votes, 2)}% ({candidate_2_votes})\n'
f'{candidates_list[2]}: {round(candidate_3_votes * 100/total_votes, 2)}% ({candidate_3_votes})\n'
f'-------------------------\n'
f'Winner: {winner}\n'
f'-------------------------')

print(output)
with open(outputpath, 'w') as f:
    f.write(output)