#Import modules
import os, csv
from pathlib import Path
#Name file location/path
csv_path = Path("Resources/election_data.csv")
#list varriables 
total_votes = 0
Stockham_votes = 0
DeGette_votes = 0
Doane_votes = 0
#Open election_data.csv file
with open(csv_path, newline="", encoding="utf-8") as election_data:
    #Put in file in csv reader
    csvreader = csv.reader(election_data, delimiter=",")
    #don't include header
    header = next(csvreader)
#for rows
    for row in csvreader: 
        #total_votes variable holds count of unique IDs
        total_votes +=1
        # Candidates - count # of times name appears and store in list
        if row[2] == "Charles Casper Stockham":
            Stockham_votes +=1
        elif row[2] == "Diana DeGette":
            DeGette_votes +=1
        elif row[2] == "Raymon Anthony Doane":
            Doane_votes +=1
#make dictionary from the 2 lists to find winner
candidates = ["Charles Casper Stockham", "Diana DeGette", "Raymond Anthony Doane"]
votes = [Stockham_votes, DeGette_votes, Doane_votes]
#zip together: candidate(key) & the total votes(value)
#max (of dictionary) reveals winner. Key stores the winner
dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key = dict_candidates_and_votes.get)
#find vote percentages
Stockham_percent = (Stockham_votes/total_votes)*100
DeGette_percent = (DeGette_votes/total_votes)*100
Doane_percent = (Doane_votes/total_votes)*100

#print summary table
print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {total_votes}")
print(f"Charles Casper Stockham: {Stockham_percent:.3f}% ({Stockham_votes})")
print(f"Diana DeGette: {DeGette_percent:.3f}% ({DeGette_votes})")
print(f"Raymon Anthony Doane: {Doane_percent:.3f}% ({Doane_votes})")
print(f"-------------------------")
print(f"Winner: {key}")
print(f"-------------------------")

#output the file as a txt file and print results
output_file = Path("Resources/Election_Results_Summary.txt")
with open(output_file, "w") as file:
    file.write(f"Election Results")
    file.write("\n")
    file.write(f"-------------------------")
    file.write("\n")
    file.write(f"Total Votes: {total_votes}")
    file.write("\n")
    file.write(f"-------------------------")
    file.write("\n")
    file.write(f"Charles Casper Stockham: {Stockham_percent:.3f}% ({Stockham_votes})")
    file.write("\n")
    file.write(f"Diana DeGette: {DeGette_percent:.3f}% ({DeGette_votes})")
    file.write("\n")
    file.write(f"Raymon Anthony Doane: {Doane_percent:.3f}% ({Doane_votes})")
    file.write("\n")
    file.write(f"-------------------------")
    file.write("\n")
    file.write(f"Winner: {key}")
    file.write("\n")
    file.write(f"-------------------------")