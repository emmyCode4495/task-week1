"""
This program is a simply python scripts that validates a mini store inventory
and sales report. The user enters his/her bio-data. The first conditional simply
guides against users that are below 18 years of age.
The second conditional which basically is the body of the program displays the list
of items in the store for the user to select from on selecting if the user selects
a product not in stock there is a conditional to tackle that.
After Purchase is over, the user finally gets a prompt for the amount of goods
he/she purchased
"""


# Variables to get Input from the user
first_name = input("Enter First Name: ")
last_name = input("Enter Last Name: ")
age = int(input("Enter your age: "))
gender = input("Gender(Male or Female): ")
Tel_no = int(input("Enter Your Phone Number: ")) 

# Dictionary to hold the products and their respective prices
products = {
            "Sneakers":2500,
            "Loafers":5000,
            "Dirty Jeans":4000,
            "Nike Polo":2500,
            "Superheroes shirts":7000,
            "Hats":3000,
            "Jackets":1800,
            "Suits":6700,
            "Canvas":5900,
            "Buttons":3250
            }


if age < 18:
    print("Oops! "+first_name+" "+last_name+" "+"our policy prohibits minors...")
    print()
    print("You need to be above 18 years old to access our Store")
    
# conditional For customers above 18 years
elif age > 18:
    print("----------------------------------------------")
    print("Hello "+ first_name+" "+"Welcome to our Mini store")
    print("----------------------------------------------")

# The print function that displays the products
    print("*****Available Products*****")
    for key,value in products.items():
        print("Product: "+ str(key)+"\n"+"Price: "+str(value)+"\n")

# The block that handles the User Entry
    response = "Y"
    total = 0
    while response == "Y":
            item_selected = input("Add Items to your cart: ")

            # conditional incase of incorrect input
            if item_selected not in products.keys():
                print()
                print("Entry not in the list of products...Enter a valid entry")
                print()
                continue
            print()

            # The total amount of products selected
            total = total + products[item_selected]
            print()
            response = input("Do you to shop more?(Y/N): ").upper()
            print()

# Transaction details
    print("Amount of Items: "+ str(total))
    print()

# Closing Message After Transaction completes
    print("Thanks for your patronage "+last_name+" "+"have a nice Time!")
    print()
    print("We Wish to see you again")
        
        
        
            
        
