# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 00:43:04 2024

@author: User
"""


def hello(): # Starts the creation of a function called 'hello'. 
    print("Hello")  # Once the function is called, prints "Hello".
    
def main(): # Starts the creation of a function called 'main'.
    hello()  # Once the function is called, calls out the function 'hello'.

if __name__ == "__main__": # Starts the If statement, If the current file is running on the 'main' script.
    main() # If the If statement passes, 'main' function is called.