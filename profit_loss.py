from pathlib import Path
import csv

# create a file path to csv file.
fp = Path.home() / "project_group" / "csv_reports" / "Profits_and_Loss.csv"

# read the csv file.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    #create the blank list and append the profit_loss information inside.
    profit_loss = []
    for row in reader:
        profit_loss.append([row[0],row[4]])

#this is for sorting the list whereby we have one string and one number
def sort_by_change(item):
    """
    this function will receive a list and return the second item of each list back
    There is one parameter required but in this programme it is not required
    """
    return item[1]

def profit_loss_calculator():

    """
    This function will determine whether net profit/loss is always increasing, decreasing, or fluctuating.
    It will then show you the outcomes for each scenarios respectively
    There is no parameter required
    """

    #create an empty list 
    result = []
    increasing = []
    decreasing = []

    #loop the range of sub-list in profit_loss starting on the second sub-list
    for i in range(1, len(profit_loss)):

        #store each variable in the list with its respective name. Taking from both present and previous day. 
        current_date, current_amount = profit_loss[i]
        previous_date, previous_amount = profit_loss[i - 1]

         #calculate the difference in the amount and assign it to variable "change"
        change = float(current_amount) - float(previous_amount)

        #determine whether its increasing or decreasing and append the data to its respective list
        if change > 0:
            increasing.append((current_date, round(abs(change))))
        elif change < 0:
            decreasing.append((current_date, round(abs(change))))

    #use if to make sure the difference is always increasing
    if increasing and not decreasing:
        #sort the increasing value from highest to lowest and append into the list "result"
        increasing.sort(key=sort_by_change, reverse=True)
        result.append("[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
        result.append([f"[HIGHEST NET PROFIT SURPLUS] DAY: {increasing[0][0]}, AMOUNT: SGD{increasing[0][1]}"])

     #use elif to make sure the difference is always decreasing
    elif decreasing and not increasing:
        #sort the decreasing value from highest to lowest and append into the list "result"
        decreasing.sort(key=sort_by_change, reverse=True)
        result.append("[NET PROFIT DEFICIT] NET PROFIT ON EACH DAY IS LOWER THAN THE PREVIOUS DAY")
        result.append([f"[HIGHEST NET PROFIT DEFICIT] DAY: {decreasing[0][0]}, AMOUNT: SGD{decreasing[0][1]}"])

    #use else to make sure the difference is functuating
    else:
        #use loop to append every row in decreasing list into variable "result"
        for row in decreasing:
            result.append([f"[NET PROFIT DEFICIT] DAY:{row[0]}, AMOUNT: SGD{row[1]}"])

        #sort the decreasing value from highest to lowest
        decreasing.sort(key=sort_by_change, reverse=True)

        label = ""
        #use loop to loop through the first three elements in the list "decreasing"
        #use conditional to determine the label and append the list into variable "result"
        for day, amount in enumerate(decreasing[:3]):
            if day == 0:
                label = "HIGHEST"
            elif day == 1:
                label = "2ND HIGHEST"
            elif day == 2:
                label = "3RD HIGHEST"
            result.append([f"[{label} NET PROFIT DEFICIT] DAY:{amount[0]}, AMOUNT: SGD{amount[1]}"])


    #create a file path to paymentsummary.txt
    file_path = Path.home()/"project_group"/"paymentSummary.txt"

    #open the file
    with file_path.open(mode="a", encoding = "UTF-8", newline="") as file:

    #Create a writer object and named it as'writer' variable.
    #using `csv.writer()`. 
        writer = csv.writer(file)

        #use loop to write each sub-list in different row 
        #use replace to take out '"' and ',' of the string
        for row in result:
            writer.writerow([str(item).replace('"', '').replace(',', '') for item in row])   

    return result
