'''
Hello! You are now viewing the code for Vending Machine!

Created by: Brent Feir
Tutored by: Lavanya Mohan
For the completion of requirements for Intro to Programming.
'''

import sqlite3 # Import SQLite3, which is a database program.
import time # Imports a time system and delays.
con = sqlite3.connect('VendingMachineDatabase.db') # Creates the connection to the database.

firstPurchase = False # Checks if the user made their first purchase.
categorySelect = 0 # Creates a numbered way to find what table is needed is being displayed in vendingScreen()
alerts = 1 # Numbers the amounts of alerts being called.
balance = 100 # Holds the amount of money being held by user, starting at 100
categories = ["Snack", "Cold Drink", "Hot Drink", "Sweets", "Produce"]
allItems = ["Popcorn", "Potato Chips", "Cheese Puffs", "Pretzels", "Crackers", 
            "Coca-cola", "Pepsi", "Chilled Water", "Iced Coffee", "Orange Juice", 
            "Coffee", "Hot Chocolate", "Mocha", "Tea", "Chai",
            "Lollipop", "Chocolate Bar", "Chewing Gum", "Brownie", "Toffee", 
            "Apple Slices", "Pineapple Slices", "Orange", "Grapes", "Baby Carrots"] # Holds the names of the products in the table.
lowerAllItems = [items.lower() for items in allItems] # Creates the same list of products, but lowercased for comparison checking.

currentTime = time.localtime() # Finds the current time on the local computer.

def timeGreeting():
    currentHour = currentTime.tm_hour # Finds the current hour.
    goodMorning = "Good morning!" 
    goodAfternoon = "Good afternoon!"
    goodEvening = "Good evening!"
    
    # If the hour is between 0 and 11:
    if (currentHour >= 0) and (currentHour <= 11):
        # Returns a "Good morning!" statement.
        return goodMorning 
    
    # If the hour is between 12 and 17:
    elif (currentHour >= 12) and (currentHour <= 17):
        # Returns a "Good aFternoon!" statement.
        return goodAfternoon
    
    # If the hour is between 18 and 24:
    elif (currentHour >= 18) and (currentHour <= 24):
        # Returns a "Good evening!" statement.
        return goodEvening

def purchase():
    # Makes all variables below globally accessible:
    global firstPurchase
    global lastPurchase
    global balance 
    
    cursor = con.cursor() # Creates a cursor to interact with the table.
    cursor.execute("select * from VendingMachineTable") # Runs the code on the table to display all items inside.
    items = cursor.fetchall() # Places all the items of the table inside the variable of items.
    y = 0 # Creates a counter to see compare what number was selected on vendingScreen()
    
    # For every item in the variable items:
    for x in items: 
        # Add 1 to the y counter
        y += 1
        
        # If the category selected was 0, this represents the user was on the Snack page:
        if categorySelect == 0:
            # menuSelected owns the same value of the user selection on vendingScreen()
            menuSelected = selected
        
        # If the category selected was 1, this represents the user was on the Cold Drink page:
        if categorySelect == 1:
            # menuSelected owns the same value of the user selection, plus 5 to account for the previous page of items.
            menuSelected = selected + 5
        
        # If the category selected was 2, this represents the user was on the Hot Drink page:
        if categorySelect == 2:
            # menuSelected owns the same value of the user selection, plus 10 to account for the previous two pages of items.
            menuSelected = selected + 10
        
        # If the category selected was 3, this represents the user was on the Sweets page:
        if categorySelect == 3:
            # menuSelected owns the same value of the user selection, plus 15 to account for the previous three pages of items.
            menuSelected = selected + 15
        
        # If the category selected was 4, this represents the user was on the Produce page:
        if categorySelect == 4:
            # menuSelected owns the same value of the user selection, plus 20 to account for the previous four pages of items.
            menuSelected = selected + 20
            
        # If the y counter reaches the item position of menuSelected:
        if y == menuSelected: 
            # and, if the balance of the user exceeds the cost of the selected item:
            if balance > x[3]:
                # and, if the stock of the product is greater than zero:
                if x[4] > 0:
                    balance -= x[3] # Deducts the user's balance by the cost of the item.
                    cursor.execute("UPDATE VendingMachineTable SET Stock = Stock - 1 WHERE Name = ?",
                                   (x[1],)) # Updates the table to deduct one stock from the selected item.
                    con.commit # Saves the Update action to the table.
                    firstPurchase = True # Tells the program that user has already made their first purchase.
                    lastPurchase = categorySelect # Keeps the last bought item's category was.
                    
                    # Then, returns the receipt of the purchase, with details of the vending machine, time, product, and balance.
                    return f"""
════════════════════════════════════════════

BRENT'S VENDING (RECEIPT)
"Where simplicity meets vending."

Spyder-Python Branch
050 - XXX - XXXX

Time: {currentTime.tm_sec}:{currentTime.tm_min}:{currentTime.tm_hour} Date: {currentTime.tm_mon}/{currentTime.tm_mday}/{currentTime.tm_year}

You have successfully purchased 1 {x[1]}!

Charged: {x[3]:.2f} AED
Change Given: {balance:.2f} AED

Thank you for shopping at BRENT'S VENDING!

════════════════════════════════════════════                  
                      """
                # If the selected product has no more stock:
                else: 
                    # Return an insufficient stock message.
                    return f"""
════════════════════════════════════════════                  

ALERT #{alerts}:
There is insufficient stock!

════════════════════════════════════════════              
                          """
                      
            # If the selected product's price exceeds the balance of user:          
            else:
                # Return an insufficient funds message.
                return f"""
════════════════════════════════════════════                  

ALERT #{alerts}:
You have insufficient funds!

════════════════════════════════════════════                  
                      """
        # If the y counter is not the same as the item position of menuSelected:
        else:
            # Continue the for loop.
            continue
        
    cursor.close() # Closes the cursor to stop overloading.
    
def suggestion():
    # If the first purchase has been made:
    if firstPurchase == True:
        
        # If lastPurchase was 0, the user last bought from Snack:
        if lastPurchase == 0:
            # Returns a suggestion to buy a drink.
            return "(Since you bought a snack, buy a drink, cold or hot!)"
        
        # If lastPurchase was 1, the user last bought from Cold Drink:
        elif lastPurchase == 1:
            # Returns a suggestion to buy a snack.
            return "(Since you bought a cold drink, buy a snack to go along with it!)"
        
        # If lastPurchase was 2, the user last bought from Hot Drink:
        elif lastPurchase == 2:
            # Returns a suggestion to buy a snack.
            return "(Since you bought a hot drink, buy a snack to cool down!)"
        
        # If lastpurchase was 3, the user last bought from Sweets:
        elif lastPurchase == 3:
            # Returns a suggestion to buy produce.
            return "(Since you bought a sweet treat, buy produce to stay healthy!)"
        
        # If last purchase was 4, the user last bought produce:
        elif lastPurchase == 4:
            # Returns a suggestion to buy sweets.
            return "(Since you bought produce, treat yourself with a sweet treat!)"
        
    # If the user hasn't bought their first purchase:
    else:
        return "" # Returns nothing back.

def names():
    cursor = con.cursor() # Creates the cursor object to interact with the table.
    cursor.execute("select * from VendingMachineTable where Type=?", (currentCategory,)) # Tell the table to find items with the current catgeory of items.
    items = cursor.fetchall() # Puts all the selected items of the cursor into the variable items.
    menu = "" # Creates an empty variable to store and return the menu.
    y = 0 # Creates a counter to number the items in the vending menu.
    
    # For every item inside items:
    for x in items:
        # Add one to the y counter.
        y += 1
        # Add the product's number, name, price, and stock to the menu.
        menu += f"[{y}] {x[1]} | Price: {x[3]:.2f} AED | Stock: {x[4]}\n"
    
    cursor.close() # Closes the cursor to stop overloading.
    return menu # Return the menu content of the current page.

        
def increaseStock():
    global alerts # Makes alerts globally accessible.
    cursor = con.cursor() # Creates a cursor to interact with the table.
    cursor.execute("select * from VendingMachineTable") # Gets all items inside of the table.
    items = cursor.fetchall() # Stores all the items in cursor to the variable items.
    menu = "" # Creates an empty variable to store the listed products.
    
    # For every item inside of items:
    for x in items:
        # Adds the item's name and stock count to the menu variable.
        menu += f"{x[1]} | Stock: {x[4]}\n"
    
    # Prints out a welcome message with a list of items in the table. 
    print(f"""
══════════════════⊱༒︎ B ༒︎⊰═════════════════

Welcome to the Brent Stock Market of Items!

{menu}

════════════════════════════════════════════ 

Which product would you like to add stock? (Enter product name)
          """)
          
    # Creates an infinite loop:
    while True:
        whichStock = str(input()) # Asks the user to which product to add stock to, and stores it in whichStock.
        # If the inputted stock by the user (lowercased) is the same as any of the lowercased items in the table's list:
        if whichStock.lower() in lowerAllItems:
            # Break the infinite loop.
            break
        # If there are no matches:
        else:
            # Prints an error message with probable reasons, asks the user to input again.
            print(f"""
════════════════════════════════════════════                   

ALERT #{alerts}:
Unrecognized product, mispell or wrong input? Try again:                  
                  
════════════════════════════════════════════ 
                  """)
            alerts += 1 # Adds a tally to the amount of alerts.
            continue # Continues the loop.
            
    # After getting the product name, asks the user how many stocks will be added.
    print("""
════════════════════════════════════════════           

How much stock would you like to add?           

════════════════════════════════════════════           
          """)
    
    # Creates an infinite loop:
    while True:
        # If there are no errors, then execute:
        try:
            howMuchStock = int(input()) # Asks the user for how many stocks to add, then making the number an integer.
            break # Breaks the infinite loop.
            
        # If there is an error, then execute:
        except:
            # Displays the error of an invalid numebr, asks the user to input again.
            print(f"""
════════════════════════════════════════════           
     
ALERT #{alerts}:     
Invalid number input, enter a valid number. Try again:         

════════════════════════════════════════════                    
                  """)
            alerts += 1 # Adds a tally to alerts.
                  
            continue # Continue the loop.
    
    # Updates the table to add the inputted amount of stock of the user's selection (lowercased) to the table.
    cursor.execute("UPDATE VendingMachineTable SET Stock = Stock + ? WHERE Name = ?",
                   (howMuchStock, (allItems[lowerAllItems.index(whichStock. lower())]),)) 
    con.commit # Saves the changes made using the Update.
    
    # Print a success message, detailing what and how much was added.
    print(f"""

Successfully added {howMuchStock} to {whichStock}!
          
════════════════════════════════════════════          
          """)
    cursor.close() # Closes the cursor connetcion to prevent overloading.
    
def increaseBalance():
    global alerts # Makes the alerts globally accessible.
    global balance # Makes the balance variable globally editable.
    
    # Print a welcome message, also asking how much money to deposit inside of balance.
    print("""
          
══════════════════⊱༒︎ B ༒︎⊰══════════════════

Welcome to the Bank of Brent, how much money
would you want to deposit?

          
          """)
          
    # Creates an infinite loop.
    while True:
        # If there are no errors, execute:
        try: 
            addMoney = int(input()) # Asks for the user's input, makes it an integer, and adds it to addMoney variable.
        # If there's an error, execute:
        except:
            # Prints an invalid number input, and asks the user to add enter their input again.
            print(f"""
════════════════════════════════════════════           
   
ALERT #{alerts}:
Invalid number input, enter a valid number. Try again:         

════════════════════════════════════════════ 
            """)
            alerts += 1 # Adds a tally to alerts.
            
    balance += addMoney # Adds the amount of money added by the user to their balance.
    # Prints a message detailing how much money was deposited and the final balance.
    print(f"""
          
You have deposited: {addMoney} AED
Your new balance: {balance} AED  
          
════════════════════════════════════════════          
          """)

def vendingScreen():
    # Makes all the variables below globally accessible:
    global alerts
    global selected
    global categorySelect
    global currentCategory
    
    # Creates an infinite loop:
    while True:
        # Finds what category is being shown and stores it in currentCategory.
        currentCategory = categories[categorySelect]
        # Prints the list of products of the selected category, an option to leave, an option to change category, as well as a suggestion.
        print(f"""
══════════════════⊱༒︎ B ༒︎⊰══════════════════

{names()}
════════════════════════════════════════════

Current Category: {categories[categorySelect]}

════════════════════════════════════════════

What would you like to buy?
[9] Next Category
[0] Exit Buy Menu

{suggestion()}

          """)
        # If there are no errors, execute:
        try:
            selected = int(input()) # Takes the user input and stores it in selected.
        # If there are errors, execute:
        except:
            # Prints an error message saying the user entered an invalid input, asks the user to input again.
            print(f"""
                  
════════════════════════════════════════════

ALERT #{alerts}:
You have entered an invalid number! Enter input again:

════════════════════════════════════════════
                  
                  """)
            alerts += 1 # Adds a tally to alerts.
            continue
                  
        # If the selected prompt has the numbers 1, 2, 3, 4, 5, 9, or 0:
        if selected in [1, 2, 3, 4, 5, 9, 0]:
            # If the selection was from one through five, then the user chose a product:
            if selected in [1, 2, 3, 4, 5]:
                print(purchase()) # Prints the whatever the purchase function returns.
                time.sleep(5) # The program waits for five seconds before moving on.
                
            # If the selecton was nine, then the user wants to change the category being displayed:
            elif selected == 9:
                # If the selection was four:
                if categorySelect == 4:
                    categorySelect = 0 # Change the category back to zero.
                # Else, if the selection was a number between zero and three:
                elif categorySelect in [0, 1, 2, 3]:
                    categorySelect += 1 # Add one to the category selection.
            
            # If the selection was zero, then the user wants to exit the buy menu:
            elif selected == 0: 
                print("Returning to Home Screen..") # Informs the user they're leaving the buy menu.
                time.sleep(3) # The program waits for three seconds before moving on.
                break # Breaks the infinite loop.
        
        # If the selection was not 1, 2, 3, 4, 5, 9, or 0:
        else:
            # Tells the user that they entered a number not listed, and asks to input again.
            print(f"""
                  
════════════════════════════════════════════

ALERT #{alerts}:
You have entered a number not listed. Enter input again:

════════════════════════════════════════════

                  """)
            alerts += 1 # Adds a tally to alerts.
            continue # Continues the loop again from the start.
    
def vendingUI():
    global choice # Makes the choice variable globally acccessible.
    global alerts # Makes alerts globally accessible.
    
    # Starts an infinite loop:
    while True:
        # Prints a greeting message and balance check, then provides options for the user to pick.
        print(f"""
══════════════════⊱༒︎ B ༒︎⊰═════════════════

{timeGreeting()} Your balance is: {balance:.2f} AED
What would you like to do?

════════════════════════════════════════════

[1] Buy from Vending Machine
[2] Increase Balance
[3] Increase Stock
[4] Exit Vending Machine

════════════════════════════════════════════

            """)
    
        choice = int(input()) # Receives input from the user, and stores it in choice.
        # If the input has a number between one through four:
        if choice in [1, 2, 3, 4]:
            # and, if the input was one, the user wants to buy from the vending machine:
            if choice == 1:
                vendingScreen() # Calls the vendingScreen function.
            
            # and, if the input was two, the user wants to increase their balance:
            elif choice == 2:
                increaseBalance() # Calls the increaseBalance function.
                time.sleep(4) # The program waits four seconds.
            
            # and, if the input was three, the user wants to increase stock:    
            elif choice == 3:
                increaseStock() # Calls the increaseStock function.
                time.sleep(4) # The program waits four seconds.
            
            # and, if the input was four, the user wants to exit the program:
            elif choice == 4:
                # Prints a thank you message to the user.
                print("""
                          
Thank you for visiting!
                          """)
                break # Breaks the last loop, finishing the program.
        
        # If the input was not a number from one through four:
        else:
            # Informs the user that they entered an invalid input, reminding them of the supposed input.
            print(f"""
                  
════════════════════════════════════════════

ALERT #{alerts}:
You have entered an invalid input! Select a number from 1-4.

════════════════════════════════════════════

                  """)
            alerts += 1 # Adds a tally to alerts.
            continue # Continues the loop.

def startVending():
    # Prints a welcome message on start up, displaying "Brent's Vending" and the credits.
    print("""
════════════════════════════════════════════════════════ ⋆★⋆ ═══════════════════════════════════════════════════════════
 @@@@@@@  @@@@@@@  @@@@@@@@ @@@  @@@ @@@@@@@  @@  @@@@@@      @@@  @@@ @@@@@@@@ @@@  @@@ @@@@@@@  @@@ @@@  @@@  @@@@@@@ 
 @@!  @@@ @@!  @@@ @@!      @@!@!@@@   @@!   !@  !@@          @@!  @@@ @@!      @@!@!@@@ @@!  @@@ @@! @@!@!@@@ !@@      
 @!@!@!@  @!@!!@!  @!!!:!   @!@@!!@!   @!!        !@@!!       @!@  !@! @!!!:!   @!@@!!@! @!@  !@! !!@ @!@@!!@! !@! @!@!@
 !!:  !!! !!: :!!  !!:      !!:  !!!   !!:           !:!       !: .:!  !!:      !!:  !!! !!:  !!! !!: !!:  !!! :!!   !!:
 :: : ::   :   : : : :: ::: ::    :     :        ::.: :          ::    : :: ::: ::    :  :: :  :  :   ::    :   :: :: : 
                                                                                                                        
═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
                                                                                 - Created and developed by Brent A. Feir
            """)
    time.sleep(2) # The program waits two seconds before moving on.
    
    # Creates an infinite loop:
    while True:
        vendingUI() # Calls the vendingUI function, starting the program.
        
        # If the choice in vendingUI was four, then the user wants to exit the program:
        if choice == 4:
            break # Breaks the loop, finishing the program.
        # If the choice was anything else:
        else:
            continue # The loop continues, goes back to vendingUI

startVending() # Calls the startVending function to greet the user and start the program.
con.close() # This line executes assuming that startVending has finished and closes the connection between the database and program.
