from pathlib import Path
import csv

# create a file path to csv file.
fp = Path.home() / "project_group" / "csv_reports" / "Cash_on_Hand.csv"

# read the csv file.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    #create the blank list and append the cash on hand information inside.
    cash_on_hand = []
    for row in reader:
        cash_on_hand.append([row[0],row[1]])


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
    result = []
    increasing = []
    decreasing = []

     #loop the range of sub-list in cash on hand starting on the second sub-list
    for i in range(1, len(cash_on_hand)):

        #store each variable in the list with its respective name. Taking from both present and previous day. 
        current_date, current_amount = cash_on_hand[i]
        previous_date, previous_amount = cash_on_hand[i - 1]

        #calculate the difference in the amount and assign it to variable "change"
        change = float(current_amount) - float(previous_amount)

        #determine whether its increasing or decreasing and append the data to its respective list
        if change > 0:
            increasing.append((current_date, round(abs(change))))
        elif change < 0:
            decreasing.append((current_date, round(abs(change))))

    #use if to make sure its always increasing


        #sort the increasing value from highest to lowest
    increasing.sort(key=sort_by_change, reverse=True)
    result.append(["[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY"])
    result.append([f"[HIGHEST CASH SURPLUS] DAY: {increasing[0][0]}, AMOUNT: SGD{increasing[0][1]}"])

    
    # elif decreasing and not increasing:
    #     decreasing.sort(key=sort_by_change, reverse=True)
    #     result.append("[CASH DEFICIT] CASH ON EACH DAY IS LOWER THAN THE PREVIOUS DAY")
    #     result.append([f"[HIGHEST CASH DEFICIT] DAY: {decreasing[0]}, AMOUNT: SGD{decreasing[1]}"])


    # else:
    #     for row in decreasing:
    #         result.append([f"[CASH DEFICIT] DAY:{row[0]}, AMOUNT: SGD{row[1]}"])
    #     decreasing.sort(key=sort_by_change, reverse=True)
    #     label = ""
    #     for day, amount in enumerate(decreasing[:3]):
    #         if day == 0:
    #             label = "HIGHEST"
    #         elif day == 1:
    #             label = "2ND HIGHEST"
    #         elif day == 2:
    #             label = "3RD HIGHEST"
    #         result.append([f"[{label} CASH DEFICIT] DAY:{amount[0]}, AMOUNT: SGD{amount[1]}"])
    return result

print(profit_loss_calculator())