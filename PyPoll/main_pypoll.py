import os
import csv

election_data = 'resources_pypoll/election_data.csv'

vote_count = 0
T_vote_count = 0


candidate_dict = {}

with open(election_data, 'r') as csvfile:
    
    election_reader = csv.reader(csvfile, delimiter = ',')
    next(election_reader)
    
    print('Election Results')
    print('----------------------------')

    for row in election_reader:
        #print(row)

        T_vote_count += 1
        
        next_name = row[2]
        
        if next_name in candidate_dict:
            candidate_dict[next_name] += 1
        
        else:
            
            candidate_dict[next_name] = 1

# Total Votes:
print(f'Total Votes: {T_vote_count}')

print('----------------------------')

# Cadidates names, vote percentage, votes per candidate:

two = []
for key in candidate_dict:
    
    # bc of percentage format function, cannot mutiple by 100
    vote_percent = (candidate_dict[key]/T_vote_count)
    
    # code reference for percent.format: https://stackoverflow.com/questions/5306756/how-to-print-a-percentage-value-in-python
    vote_p = '{:.3%}'.format(vote_percent)
    print(f'{key}: {vote_p}  ({candidate_dict[key]})')
    two_keys = f'{key}: {vote_p}  ({candidate_dict[key]})'
    two.append(two_keys)

    
# code referece for .get function: https://www.entechin.com/how-to-find-the-max-value-in-a-dictionary-in-python/#:~:text=The%20simplest%20way%20to%20get,max%20value%20of%20any%20iterable.
max_val = max(candidate_dict, key = candidate_dict.get)

print('----------------------------')

print(f'Winner: {max_val} ')

print('----------------------------')



intro = 'Election Results'
line = "--------------------------------------"
one = f'Total Votes: {T_vote_count}'

line = "--------------------------------------"
three = f'Winner: {max_val} '

txt_file = open("pypoll.txt", 'w')

txt_file.write(f"{intro}\n{line}\n{one}\n{line}\n")

# to print all values that were appended to my 'two' list, which are coming from my 'candidate_dict'- dictionary 
for value in two:
    txt_file.write(f"{value}\n")
    
txt_file.write(f"{line}\n{three}\n{line}")
txt_file.close()
