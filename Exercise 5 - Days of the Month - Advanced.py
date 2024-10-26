# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 23:46:13 2024

@author: User
"""
months = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
    } # Creates a dictionary containing the key as the month and the value as the amount of days within that month.

UserMonth = int(input("Enter a number corresponding to a month in a year (1-12): ")) # Asks the user to enter a number corresponding to the year, stores it in 'UserMonth'.
if UserMonth < 13 and UserMonth > 0: # Checks if 'UserMonth' is within the range of 1-12
    if UserMonth == 2: # Starts the If statement, If 'UserMonth' is equal to two, which is February.
        isLeap = input("Is the year a leap year? Y/N ") # Asks the user if the the February takes place in a leap year, stores it in 'isLeap'.
        if isLeap.lower() == 'y': # Starts the If statement, If the input (lowercased), is equal to 'y' (which means yes)
            print(29) # If the If statement passes, then the output is '29', in reference to February in a leap year.
        else:
            print(28) # If the If statement fails, then the output is '28', in reference to Februaru in a normal year.
    else:
        print(months[UserMonth]) # If 'UserMonth' is not two (February), then it gets the location of the input within 'months'.
else:
    print("Number is not within 1-12!") # If the number inputted is not within 1-12, prints an error message.