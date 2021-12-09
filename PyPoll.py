#Add our dependencies
import csv
import os
#Assign a variable to load a file
file_to_load = os.path.join("Resources","election_results.csv")
#Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Open the election results and read the file 
with open(file_to_load) as election_data:
    # To do: read and analyze the data here
    #Read the file object with the reader function
    file_reader = csv.reader(election_data)
    #Print each row in the CSV file
    headers = next(file_reader)
    print(headers)


# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won 
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote










#BELOW STARTS PRACTICE CODE (DISREGARD FOR ANALYSIS)
    #print(election_data)
#Use the with statement to open the file as a text file
#with open(file_to_save, "w") as txt_file:
    #Write some data to the file
    # txt_file.write("Counties in the Election\n----------------\nArapahoe\nDenver\nJefferson")

#import datetime as dt
#now = dt.datetime.now()
#print("the time right now is", now)

#import csv 
#dir(csv)
# dir(str)
#import os 
#os.path.join("Resources", "election_results.csv")
#file_to_load = os.path.join("Resources", "election_results.csv")
