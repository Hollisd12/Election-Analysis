# Election Analysis

## Project Overview
In this project, we assisted a Colorado Board of Electionsemployee, Tom, perform an election audit of the tabulated results for a U.S. congressional election in Colorado. With the use of python, we are tasked with evaluating the voter data and extracing the following data:

1. The total number of votes cast
2. A list of candidates who received votes
3. The total number of votes each candidate received
4. The percentage of votes each candidate won
5. The winner of the election based on popular vote
6. The voter turnout for each county
7. The percentage of votes from each country out of the total count
8. The county with the highest turnout

## Resources
- Data Source: election_results.csv
- Software: Python 3.6.1, Visual Studio Code 1.71.2

## Election Audit Results
We used the code below to Analyze the total number of votes, get a list of candidates who received votes, and their total votes. We used a for loop to to determine the total votes in the election, every row was counted as one vote. For a list of candidates, we used the for loop with an if statement to determine the candidates that received votes. Every time a candidate is listed, a vote for that candidate is added. 

![Code_1](https://user-images.githubusercontent.com/112137694/193700518-2df982b5-4a5f-4741-86f3-6ea7b7bacf50.png)

The results of the script are as follows:
- There were 369,711 votes cast in the election
- The candidates were:
  - Charles Casper Stockham who received 85,213 votes
  - Diana DeGette who received 272,892 votes
  - Raymond Anthony Doane who received 11,892

We used the code below to calculate each candidate's results. A for loop is used to loop through each candidate and their votes. We calculate the percentage of each candidate's and use an if statement to determine the winner. 

![Code_2](https://user-images.githubusercontent.com/112137694/193700742-4f84fc20-ee6b-45da-a2a4-03aabb080a80.png)

The candidate results were as follows:
  - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes
  - Diana DeGetter received 73.8% of the vote and 272,892 number of votes
  - Raymond Anthony Doane received 3.1% of the vote and 11,692 number of votes

The winner of the election was:
  - Diana DeGette, who received 73.8& of the vote and 272,892 number of votes

We used the script below to calculate the voter tunrout for each county. Similar to calculating the candidate results, we used a foor loop to loop through each county and their votes to calculate the percentage of each county's votes compared to the total votes cast. Then we use an if statement to determine the county with the highest voter turnout. 

![Code_3](https://user-images.githubusercontent.com/112137694/193700916-31b73ada-0958-46e9-8050-88fc12639908.png)

The voter turnout for each county was:
  - Jefferson voters accounted for 10.5% of the vote with 38,855 number of votes
  - Denver voters accounted for 82.8% of the vote with 306,055 number of votes
  - Arapahoe voters accounted for 6.7% of the vote with 24,801 number of votes

The county with the highest turnout was:
  - Denver with 82.8% of the voters with 306,055 number of votes

## Election Audit Summary
As we have successfuly audited the congressional vote data using Python, we can apply the same code to automate future elections on the senatorial and local level. To use our script to analyze future elections, modifications will be required. First, the file_to_load and file_to_save paths will need to be updated to reflect the data source for the future election. Additionally, if the election is on a presidential level, more code can be added to calculate the total votes per state, demographic, etc. 
