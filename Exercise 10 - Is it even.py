# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 16:13:50 2024

@author: User
"""

def evenorodd(a): # Creates a function called 'evenorodd', with a parameter of 'a'.
    if (a%2 == 0): # Starts an If statement, If variable 'a', modulo of two, is equal to zero. 
        print("Your number is even!") # If the If statement passes, prints that the 'a' is even.
    else:
        print("Your number is odd!") # If the If statement passes, prints that the 'a' is odd.

user = int(input("Enter number: ")) # Asks the user to enter a number, and converts it to integer format, and stores it in 'user'.
evenorodd(user) # Calls out the 'evenorodd' function, with an input of 'user'.