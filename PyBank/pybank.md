One of the most useful things I found for this assignment was the:

if 'variable' is not None:

This if statement allowed me keep track of my values in both the row[0] and row[1] in the CSV file so I could calculate the greatest increase and decrease in profits as well as when they occured. 

    I did this by appending a list for dates and profits/losses.

    For the first iteration of my for loop, when the loop came accross the variables within the if-not None statements, it ignored the variables because it had a value of zero, or 'None'. 
    
    I had to then make sure to assign a value to the variables after the if-not None statement, so for follwing iterations the conditions within these if-not None statements would occur. 


After I had kept track of the values for both columns and created my list (and thanks to the if-not None statements they lined up with eachother)- it mostly was simple math and print statements.

The last slightly tricky thing to solve for was assigning the greatest increase/ decrease of Profits to their respective dates.

    I made sure to find the index for the max and min values for the Profit/Losses columns within the new list I created.

    I then made sure to create an if-statement that said if the index of my new date column list equaled the index value for the max and min of my new Profit/Losses list to:

        Print out that date and the max/min associated with it