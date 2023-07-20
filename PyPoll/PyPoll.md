This exercise was difficult as I could not keep track of the cadidates' names in the same manner as previous exercises.

I started by keeping track of rows. Once the value of a row was different than the previous row I added it to a list. The issue was that there were only a total of three candidates and the CSV files were not organized. So I receive everyone's name twice, because the names appeared x-amount of times only to appear again after other candidates' names. 

I resolved by:

    First, I created an empty dictionary

    I then assigned a variable that held the candidate name that was in whatever row the iteration was on

    Then, I created an if-statement that essentially said, if the candidate's name was not in the dictionary, add it as the key and give it a value of 1

    If the name was in the dictionary add and assign another 1 

    This allowed me to keep track and consolidate the names as well as keep their count

The next difficult thing to do was to print the candidate name, the percentage of votes they won, as well as the total numerical votes they won. 

Thanks to the if-statement I created prior I was able to:

    Divide the value of the key by the overall total votes, which I also kept track of, to get the voting percentage

    I then created a variable from a for loop, which stored the key from the dictionary which was also the candidate's name

    This for-loop will allow me to iterate the dictionary only the amount of times there are keys/ candidated names

    Lastly, within a for loop, I just needed to create a f-string within a print function that incorporated the 'key variable'/ candidate's name, the voting percentage calculated, and the dictionary's key's value


My last issue was when I was creating a text file. I was having difficulty getting the candidate's names and votes. 

I resolved this by creating a list, I appended this list with a variable that contained my f-string and kept it in the for-loop I previously mentioned. 

I then iterated this new list when writing onto the txt file I created


Here are the sources I used for certain pieces of code:

code reference for percent.format: https://stackoverflow.com/questions/5306756/how-to-print-a-percentage-value-in-python

code referece for .get function: https://www.entechin.com/how-to-find-the-max-value-in-a-dictionary-in-python/#:~:text=The%20simplest%20way%20to%20get,max%20value%20of%20any%20iterable.
