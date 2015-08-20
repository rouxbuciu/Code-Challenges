# ============================================================================
# Product Inventory Project
#
# Project: Create an application which manages an inventory of products.
# Create a product class which has a price, id, and quantity on hand. Then
# create an inventory class which keeps track of various products and can sum
# up the inventory value.
#
# Personal goals for this project:
# - Design a menu system
# - Learn to use Try/Except to make sure user inputs valid things
# - **Minor Goal** Learn how to save/read user data to a file for future use
# ============================================================================

# Import the modules needed to run the script.
import sys
import os
import time
import pickle

# =======================
#       CONSTANTS
# =======================

menu_actions  = {}
productList = []


# =======================
#       CLASSES
# =======================

class Product(object):
    """Products that a store has. Adding products in done by using the
    add_product() function.

    Attributes:
    Name - product name or id number
    Price - product price
    Quantity - the amount of the product on hand
    """

    def __init__(self, name, price, quantity):
        """Return a product with a name, price and quantity."""
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_price(self, new_price):
        """Function to update the price of a product."""
        self.price = new_price

    def update_quantity(self, new_quantity):
        """Function to update the quantity of a product."""
        if self.quantity + new_quantity < 0:
            print "Quantity would be reduced below zero."
            time.sleep(2)
        else:
            self.quantity += new_quantity


class Inventory(Product):
    """Keeping track of everything that we have on hand."""

    def __init__(self):
        pass

    # Seeing a printout of all products & their attributes
    def view_inventory(self, inventory):
        for prod in inventory:
            print prod.name.title(), prod.price, prod.quantity
        return

    # User can search by specific product names
    def lookup_inventory(self, inventory):
        lookup = raw_input("Enter product to lookup:\n")
        for prod in inventory:
            if lookup in prod.name:
                print "%s\nPrice: %s      Quantity: %s" % (prod.name.title(),
                        prod.price, prod.quantity)
        return

    # Adding new products to inventory
    def add_prod(self, inventory):
        name = raw_input("Enter product name: ").lower()
        while True:
            try:
                price = float(raw_input("Enter product price: "))
                break
            except ValueError:
                print "Please enter an appropriate value."
        while True:
            try:
                quantity = int(raw_input("Enter item quantity: "))
                break
            except ValueError:
                print "Please enter a valid quantity."

        if verification() == 'y':
            inventory.append(Product(name, price, quantity))

    # Removing exitsing products from inventory
    def remove_prod(self, inventory):
        temp = []
        for e in inventory:
            temp.append(e.name)
        while True:
            product = raw_input(" >> ").lower()
            if product in temp:
                if verification() == 'y':
                    inventory.pop(temp.index(product))
                    print "Removing %s." % product
                    time.sleep(1)
                    break
            elif product not in temp:
                print "Product not found."
                time.sleep(1)


# =====================
#      FUNCTIONS
# =====================

# Create new Product instances
def add_product():
    Inventory().add_prod(productList)
    exec_menu('p')
    return

# Removing a product from the productList
def remove_product():
    print "Enter product to remove from inventory:"
    Inventory().remove_prod(productList)
    exec_menu('p')
    return

def change_price():
    print "Enter product name:"
    while True:
        lookup = raw_input(" >> ").lower()
        try:
            for prod in productList:
                if lookup == prod.name:
                    break
                break
            break
        except:
            print "Please enter a valid product name."
    print prod.name.title()
    print "Current price: %s" % prod.price
    print "\n Enter new price:"
    while True:
        try:
            new_price = float(raw_input(" >> "))
        except ValueError:
            "Please enter a valid price."
    if verification() == 'y':
        prod.update_price(new_price)
    exec_menu('p')
    return

def change_quantity():
    print "Enter product name:"
    while True:
        lookup = raw_input(" >> ").lower()
        try:
            for prod in productList:
                if lookup == prod.name:
                    break
                break
            break
        except:
            print "Please enter a valid product name."
    print prod.name.title()
    print "Current quantity: %s" % prod.quantity
    print "\nEnter quantity to add or substract from current stock:"
    while True:
        try:
            new_quantity = int(raw_input(" >> "))
            break
        except ValueError:
            print "Pleave enter a valid quantity"
    if verification() == 'y':
        prod.update_quantity(new_quantity)
    exec_menu('i')
    return

# Display all information about all products
def view_all_inventory():
    Inventory().view_inventory(productList)
    done = raw_input("[Enter to return to menu.]")
    exec_menu('i')
    return

# Only display information about specific product user searches for
def lookup_product():
    Inventory().lookup_inventory(productList)
    done = raw_input("[Enter to return to menu.]")
    exec_menu('i')

# Checking with users if the information they entered is correct
# using a simple yes or no function
def verification():
    print "Are you sure? (y/n)"
    while True:
        verify = raw_input(" >> ").lower()
        try:
            if verify in ('y', 'n'):
                break
        except:
            print "Please enter a valid answer"
            time.sleep(1)
    return verify


# =======================
#     MENUS FUNCTIONS
# =======================

# Main menu
def main_menu():
    os.system('clear')

    print "Product Inventory Project \n"
    print "Please choose what menu you require:"
    print "[p] Product Management Menu"
    print "[i] Inventory Management Menu"
    print "\n[f] Info"
    print "[q] Quit"
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return

# Execute menu
def exec_menu(choice):
    os.system('clear')
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print "Invalid selection, please try again.\n"
            menu_actions['main_menu']()
    return

# Product Menu
def menu_product():
    print "Product Management\n"
    print "[a] Add Product"
    print "[u] Update Product Price"
    print "[r] Remove Product"
    print "\n[b] Back"
    print "[q] Quit"
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return

# Menu 2
def menu_inventory():
    print "Inventory Management\n"
    print "[n] Update Product Quantity"
    print "[l] Lookup item in inventory"
    print "[v] View Complete Inventory\n"
    print "\n[b] Back"
    print "[q] Quit"
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return

# About menu
def about():
    print """
    Product Inventory Project
    v 0.9

    created 19/08/2015

    all coding by
    everybody_codes


    www.thecrunge.org


    (c) 2015 Roux G. Buciu"""
    choice = raw_input("")
    exec_menu('main_menu')

# Back to main menu
def back():
    menu_actions['main_menu']()

# Exit program
def exit():
    sys.exit()


# =======================
#       DEFINITIONS
# =======================

# Menu definition
menu_actions = {
    'main_menu': main_menu,
    'p': menu_product,
    'i': menu_inventory,
    'r': remove_product,
    'u': change_price,
    'n': change_quantity,
    'v': view_all_inventory,
    'l': lookup_product,
    'a': add_product,
    'f': about,
    'b': back,
    'q': exit,
}


# =======================
#      MAIN PROGRAM
# =======================

# Main Program
if __name__ == "__main__":
    # Launch main menu
    main_menu()
