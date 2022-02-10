# Election Analysis
Analysis of Recent Local Congressional Election Data Using Python 

## Project Overview
A Colorado Board of Elections employee has given me the following tasks to complete the election audit of a recent local congressional election. 

Candidate-Based Analysis
1. Calculate total number of votes cast.
2. Get complete list of candidates who received votes.
3. Calculate total number of votes each candidate won.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

County-Based Analysis
1. Calculate the voter turnout for each county
2. Calculate the percentage of votes from each county out of the total count
3. Determine the county with the highest turnout

### Resources
* Data Source: election_results.csv
* Software: Python 3.8.9, Visual Studio Code, 1.63.0

## Election Audit Results
### Candidate-Based Analysis
The analysis of the election show that:
* There were 369,711 votes cast in the election. 
* The candidates were:
  * Charles Casper Stockham
  * Diana DeGette
  * Raymon Anthony Doane
* The candidate results were: 
  * Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
  * Diana DeGette received 73.8% of the vote and 272,892 number of votes.
  * Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
* The winner of the election was: 
  * Diana DeGette, who received 73.8% of the vote and 272,892 number of votes. 

### County-Based Analysis
The analysis of the election show that: 
* The county results were:
  * Jefferson county received 10.5% of the votes with 38,855 total votes.
  * Denver county received 82.8% of the votes with 306,055 total votes.
  * Arapahoe county received 6.7% of the votes with 24,801 total votes.
* The county with the largest voter turnout was Denver. 

## Election Audit Summary
The script created in this analysis is beneficial because it can be used to analyze the results of any election.
Depending on whether the election being analyzed is a presidential, congressional, state, or local election, certain variables can be modified to match the data that is being used. 
For example, if we are looking at a presidential election, instead of look at "county_votes" and the "county_options", we can change the variables to "state_votes" and "state_options" and be sure to adjust the names down the script. 

* x = variable to be modified depending on dataset being used
```
Create a county list and county votes dictionary.
x_options = []
x_votes = {}
Track the largest county and county voter turnout.
winning_x = ""
winning_x_count = 0 
```
It is important to also take a look at how the new set of data is organized, depending on the ways in which it is organized we can modify the index when attempting to extract the "candidate" and/or "state" names from each row:

* x = index to be modified depending on dataset being used
```
Get the candidate name from each row.
candidate_name = row[x]
Extract the county name from each row.
state_name = row[x]
```
Also, at the very beginning of the script, where the file path to the dataset is being given. The correct filepath must be outline in order to be able to open and acces the dataset. 

* x = filepath to be modified depending on dataset being used
```
Add a variable to load a file from a path.
file_to_load = os.path.join("x", "x.csv")
```

