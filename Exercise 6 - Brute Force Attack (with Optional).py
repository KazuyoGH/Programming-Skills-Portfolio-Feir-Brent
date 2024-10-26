# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 00:11:25 2024

@author: User
"""

correctpass = "12345" # Creates a variable that stores the password called 'correctpass'.
attempts = 5 # Creates a variable that stores teh amount of attempts the user can make called 'attempts'.

while attempts > 0: # Starts a while statement, where 'attempts' is greater than zero.
    guess = input("Enter your password: ") # Asks the user to enter a password attempt, stores it in 'guess'.
    if guess == correctpass: # Starts the If statement, If 'guess' is the same as 'correctpass'.
        print("Password successfully matched!") # If the If statement passes, then prints a success message.
        break # Breaks the while loop immediately.
    else:
        attempts -= 1 # If the If statement fails, then decrease the amount of attempts by 1.
        print("Incorrect, you have " + str(attempts) + " attempts left.") # Prints an incorrect message, and then lists how many attempts there are left.
        
if attempts == 0: # Starts an If statement, If 'attempts' is equal to zero.
    print("Maximum amount of attempts reached, contacting authorities.") # Prints to the user that the max amount of attempts have been used, and authroities are called.