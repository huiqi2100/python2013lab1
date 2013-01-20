# Filename: master_or_visa.py
# Date created: 18 Jan 2013
# Author: Koh Hui Qi
# Description: Differentiate a card number input between MasterCard and VISA

# (a) Devise an algorithm to categorize if a user input credit card number
#  belongs to MasterCard or VISA.

def morv(cardno):
    cardno = str(cardno)
    if len(cardno) == 16: # check for 16 digits
        # check first digit to distinguish between VISA/MasterCard
        if cardno[0] == "5": 
            print("Master card")
        elif cardno[0] == "4":
            print("Visa")
        else:
            print("Neither Master card nor Visa.")
    else:
        print("Invalid card input. Needs to be 16 digits.")

#  (b) Implement your algorithm in (a) as master_or_visa.py

cardno = input("Please enter card number:")

morv(cardno)


