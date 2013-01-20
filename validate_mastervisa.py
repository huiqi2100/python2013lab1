# Filename: master_or_visa.py
# Date created: 18 Jan 2013
# Author: Koh Hui Qi
# Description: Validate a MasterCard and VISA card number input 


# (c) Devise an algorithm to validate a user input MasterCard or
#     VISA credit card number.

def validate_card(cardno):
    cardno = str(cardno)
    # check for 16 digits
    if len(cardno) == 16:
        if cardno.isdigit():
            if cardno[0] == "4":
                print("Valid VISA card number")
            elif cardno[0] == "5":
                print("Valid MasterCard card number")
            else:
                print("Invalid VISA/MasterCard card number")
        else:
            print("Invalid card number")
    else:
        print("Invalid card number")


# (d) Implement your algorithm in (c) as validate_mastervisa.py

cardno = input("Please enter card number to validate:")

validate_card(cardno)
