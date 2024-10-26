# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 00:38:01 2024

@author: User
"""

names = ("Jake", "Zac", "Ian", "Ron", "Sam", "Dave") # Creates a list of six different names called 'names'.
search = input("Search for what name? ") # Asks the user what name is bearing searched, stores it in 'search'.
for i in names: # For every instance in the list 'names':
    if i == search: # Starts an If statement, If any instance in 'names' is equal to 'search'.
        print(i + " is found!") # If the If statement passses, prints the instance and a message that it was found.