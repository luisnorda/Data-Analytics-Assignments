import os
import csv

#find current py's path:
#print(os.path.abspath(__file__))
# /Users/admin/Desktop/python-challenge/PyBank/main_pybank.py

#cvs's relative path:
budget_data = "resources_pybank/budget_data.csv"

m_count = 0
total_P_L_sum = 0

next_r = 0
prev_p_L = None
change_T = []

prev_name = None
change_name = []

    
with open(budget_data, 'r') as csvfile:
    
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader)
        
        print("Financial Analysis")
        print("--------------------------------------")
        
        
        for row in csvreader:
            #print(row)
            m_count = m_count + 1
        
            #addition and assignment operator (+=)
            total_P_L_sum += int(row[1])
    
            next_r = int(row[1])
            
            #in first iteration, this is none, until we assign next_r to prev_p_L at the end of this first iteration 
            if prev_p_L is not None:
                change = next_r - prev_p_L
                change_T.append(change)
                
            # need to set the previous row value within the prev_p_L variable so when it goes back to it within the iteration it has the value
            prev_p_L = next_r
            
            next_name = str(row[0])
            
            if prev_name is not None:
                n_change = next_name
                change_name.append(n_change)
                
            prev_name = next_name
            
        # the if statement is just incase the m_count is 0 (no rows in the csv file), it will then give a value of zero for the equation
        average_of_change_T = sum(change_T)/(m_count-1) if m_count else 0
        
        print(f"Total Months: {m_count}.")
        print (f"Total: {total_P_L_sum}.")
       
        
        # the ".2F" is to give less decimal values
        print(f"Average Changes: {average_of_change_T:.2F}.")
        
        #for index of max and min of change_T:
        Change_T_index_max = change_T.index(max(change_T))
        Change_T_index_min = change_T.index(min(change_T))
        
        for index,value in enumerate(change_name):
            if index == Change_T_index_max:
                print(f"The Greatest increase in Profits: {value}, {max(change_T)}.")
                # need to keep this in the if statement
                three = f"The Greatest increase in Profits: {value}, {max(change_T)}."
            if index == Change_T_index_min:
                print(f"The Greatest decrease in Profits: {value}, {min(change_T)}.")
                four = f"The Greatest decrease in Profits: {value}, {min(change_T)}."
            
# if I made these the variables for the print funcitons it would not return anything to me, so my .txt would give me values of None.
intro = "Financial Analysis"
line = "--------------------------------------"
one = f"Total Months: {m_count}."
two = f"Total: {total_P_L_sum}."




# \n signifies "next line" 
txt_file = open("pybank.txt", 'w')
txt_file.write(f"{intro}\n{line}\n{one}\n{two}\n{three}\n{four}")
txt_file.close()