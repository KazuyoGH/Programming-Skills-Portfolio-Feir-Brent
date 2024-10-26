# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 10:43:59 2024

@author: User
"""

biography = {} # Create the dictionary to store the user inputs.
biography['name'] = input("Enter your name: ") # Asks the user for input for their name.
biography['hometown'] = input("Enter your hometown: ") # Asks the user for input on their hometown. 

while True: # A looping control structure that loops forever.
    try: # Continues the next line of code.
        biography['age'] = int(input("Enter your age: ")) # Asks the user for input for their age.
        break # If the code did not encounter a value error, this breaks the loop.
    except ValueError: # If the code encountered a value error, the loop continues.
        print("Please type a number!") # This asks the user to enter their age as a number
        

print(biography['name'] + '\n' + biography['hometown'] + '\n' + str(biography['age'])) # Once the loop is broken, this prints the inputs on separate lines.