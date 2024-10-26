# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 23:13:38 2024

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
    print(months[UserMonth]) # If the input is within 1-12, then it gets the location of the input within 'months'.
else:
    print("Number is not within 1-12!") # If the number inputted is not within 1-12, prints an error message.
    