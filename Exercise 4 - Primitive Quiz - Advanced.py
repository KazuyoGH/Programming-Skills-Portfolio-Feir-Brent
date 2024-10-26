# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 22:46:36 2024

@author: User
"""
EUCountries = ["France", "Netherlands", "Spain", "Germany", "Italy", "Greece", "United Kingdom", "Poland", "Sweden", "Iceland"]
# The code above puts the names of countries in a list.
EUCapitals = ["paris", "amsterdam", "madrid", "berlin", "rome", "athens", "london", "warsaw", "stockholm", "reykavik"]
# The code above puts the names of capitals of the listed countries above.

for i in range(10): # Runs a for loop that goes 10 times.
    answer = input("What is the capital of " + EUCountries[i] + "? ") # Asks the user the capital of the country, both in relation to the current value of i, and then stores it in 'answer'.
    if answer.lower() == EUCapitals[i]: # Starts the If statement, compares if the input by the user (lowercased), is the answer from the list.
        print("Your answer is correct!") # If the If statement successes, prints the asnwer is correct.
    else:
        print("Your answer is incorrect!") # If the If statement fails, prints the answer is wrong.