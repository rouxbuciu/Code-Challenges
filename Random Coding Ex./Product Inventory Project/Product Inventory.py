# ============================================================================
# Product Inventory Project
#
# Project: Create an application which manages an inventory of products.
# Create a product class which has a price, id, and quantity on hand. Then
# create an inventory class which keeps track of various products and can sum
# up the inventory value. [x]
#
# Additional personal goals for this project:
# - Design a menu system [x]
# - Learn to use Try/Except to make sure user inputs valid things [x]
# - Learn how to save/read user data to a file for future use [x]
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
fileName = "Product Inventory.txt"


# =======================
#       CLASSES
# =======================

class Product(object):
    """Products that are being created off this template. Adding products is
done by using the add_product() function.

Product attributes:
product.name - product name or id number
product.price - product price
product.quantity - the amount of the product on hand
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
        """We don't create instances of inventory, we use it for inventory
        management purposes."""
        pass

    def view_inventory(self, inventory):
        """Generates a printout of all product instances & their attributes."""
        for prod in inventory:
            print prod.name.title(), prod.price, prod.quantity
        return

    def lookup_inventory(self, inventory):
        """Allows user to search by specific product names."""
        name, exists, prod_index = lookup()
        if len(productList) == 0:
            print "There are no products currently in the database."
            time.sleep(2)

        elif len(productList) > 0 and exists == 'n':
            print "No such product exists in the database."

        elif len(productList) > 0 and exists == 'y':
            print "Product Info: ", inventory[prod_index].name.title()
            print "Current price: %s\t Current stock: %s" % (
                    inventory[prod_index].price,
                    inventory[prod_index].quantity)
        return

    def add_prod(self, inventory):
        """ Adding new products to inventory
                Checks whether product being entered already exists
                Makes sure quantity & price are numbers"""
        while True:
            os.system('clear')
            name, exists, prod_index = lookup()
            if len(productList) > 0 and exists == 'y':
                print "Product already exists."
                time.sleep(1)
            else:
                break
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

    def remove_prod(self, inventory):
        """Removing exitsing products from inventory."""
        name, exists, prod_index = lookup()
        if len(productList) == 0:
            print "There are no products currently in the database."
            time.sleep(2)

        elif len(productList) > 0 and exists == 'n':
            print "No such product exists in the database."
            time.sleep(2)

        elif len(productList) > 0 and exists == 'y':
            if verification() == 'y':
                inventory.pop(prod_index)
                print "Removing %s.......  done" % name
                time.sleep(1)

# ==============================
#    USER - ACCESSED FUNCTIONS
# ==============================

# Create new instances of Product() (ie. new actual products)
def add_product():
    Inventory().add_prod(productList)
    exec_menu('p')
    return

# Removing a product from the productList
def remove_product():
    print "WARNING:\nRemoving a product from the database cannot be undone.\n"
    Inventory().remove_prod(productList)
    exec_menu('p')
    return

# Allows user to change the price of an already existing product
#   Checks that product exists before continuing
def change_price():
    prod, exists, prod_index = lookup()
    if len(productList) == 0:
        print "There are no products currently in the database."
        time.sleep(2)

    elif len(productList) > 0 and exists == 'n':
        print "There is no such product in the database."
        time.sleep(2)

    elif len(productList) > 0 and exists == 'y':
        print productList[prod_index].name.title()
        print "Current price: %s" % productList[prod_index].price
        print "\nEnter new price:"
        while True:
            try:
                new_price = float(raw_input(" >> "))
                break
            except ValueError:
                print "Pleave enter a valid price."
        if verification() == 'y':
            productList[prod_index].update_price(new_price)

    exec_menu('p')
    return

# Allows user to change the quantity of a product (positive or negative)
#   checks whether the product exists before anything else
def change_quantity():
    prod, exists, prod_index = lookup()
    if len(productList) == 0:
        print "There are no products currently in the database."
        time.sleep(2)

    elif len(productList) > 0 and exists == 'n':
        print "There is no such product in the database."
        time.sleep(2)

    elif len(productList) > 0 and exists == 'y':
        print productList[prod_index].name.title()
        print "Current quantity: %s" % productList[prod_index].quantity
        print "\nEnter quantity to add or substract from current stock:"
        while True:
            try:
                new_quantity = int(raw_input(" >> "))
                break
            except ValueError:
                print "Pleave enter a valid quantity"
        if verification() == 'y':
            productList[prod_index].update_quantity(new_quantity)

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

# Save product data to bundled file
def save_data():
    print "Saving product data to Product Inventory.txt"
    if verification() == 'y':
        fileObject = open(fileName, 'w')
        pickle.dump(productList, fileObject)
        fileObject.close()
    exec_menu('main_menu')

# Erase data from both internal memory and from bundled file data
def erase_data():
    print """WARNING

    This action will erase both currently stored program data as well as all
    program data stored on the disk. You cannot undo this action.

    """
    if verification() == 'y':
        del productList[:]
        fileObject = open(fileName, 'w')
        fileObject.truncate()
        fileObject.close()
    exec_menu('d')


# ======================
#   PROGRAM FUNCTIONS
# ======================

# Checking with users if the information they entered is correct or if they
# are sure they want to proceed using a simple yes or no function
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

# Useful function for checking whether a product name is in the productList
def lookup():
    while True:
        name = raw_input("Enter product name:\n >> ").lower()
        if len(productList) == 0:
            prod_exists = 'n'
            prod_index = '0'
            break
        else:
            for prod in productList:
                if name == prod.name:
                    prod_exists = 'y'
                    prod_index = productList.index(prod)
                    break
                else:
                    prod_exists = 'n'
                    prod_index = '0'
            break
    return (name, prod_exists, prod_index)


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
    print "[d] Data Management\n"
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
    print "[r] Remove Product\n"
    print "\n[b] Back"
    print "[q] Quit"
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return

# Inventory Menu
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

# Data Management Menu
def data_management():
    print "Data Management\n"
    print "[s] Save Data to Disk"
    print "[e] Erase Product Inventory\n"
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
    's': save_data,
    'e': erase_data,
    'd': data_management,
    'f': about,
    'b': back,
    'q': exit,
}


# =======================
#      MAIN PROGRAM
# =======================

# Before loading program, load any existing products
try:
    fileObject = open(fileName, 'r')
    productList = pickle.load(fileObject)
    fileObject.close()
except EOFError:
    pass

# Main program
if __name__ == "__main__":
    # Launch main menu
    main_menu()
