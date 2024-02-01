from pathlib import Path
import csv

# create a file path to csv file.
fp = Path.home() / "project_group" / "csv_reports" / "Overheads.csv"

# read the csv file.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    #create the blank list and append the overheads information inside.
    overheads = []
    for row in reader:
        overheads.append([row[0],row[1]])


def highest_overheads_calculator():
    
    """
    This function will find the highest overheads for you 
    There is no parameter required
    """

    #Arrange the overheads from highest to lowest
    highest_overheads = max(overheads)

    #assign the answer into a variable "result"
    result = [(f"[HIGHEST OVERHEAD] {highest_overheads[0]}: {highest_overheads[1]}%" )]


    #create a new txt file to write the result
    file_path = Path.home()/"project_group"/"paymentSummary.txt"
    file_path.touch()

    #open the file
    with file_path.open(mode="w", encoding = "UTF-8", newline="") as file:

    #Create a writer object and named it as 'writer' variable.
    # using `csv.writer()' and write the variable "result" inside the file
        writer = csv.writer(file)
        writer.writerow(result)  

    


