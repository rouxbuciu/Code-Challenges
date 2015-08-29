import sys
import os
import time
import pickle
import menu_services
import menu_actions
import menu_client
import menu_main
import f_classes
import menu_invoice
import f_misc_functions
import cfg
import fandango_pos
import projects

# =================================
#        SERVICES MENU
# =================================


def view_services():
    os.system('clear')
    print("\n\nService".ljust(40) + "   Price")
    print("="*45)
    for n in cfg.SERVICES:
        print("| " + str(n).ljust(38) + "| " + str(cfg.SERVICES[n]))
    print("\n\nPress [return] to go back to Services Management.")

    choice = input("")
    menu_main.execute_menu('s')


def add_service():
    new_service = input("\n\nEnter a service to add:\n\n >> ").title()
    print("\n")
    cfg.SERVICES[new_service] = int(input(
        "How much does this cost per hour?\n\n >> "))

    f_misc_functions.save_database()
    menu_main.execute_menu('s')


def remove_service():
    os.system('clear')
    print("\n\nServices currently offered:\n")
    for n in cfg.SERVICES:
        print(n)
    print("""
          *** WARNING ***
          Removing a service deletes it permanently from the database.""")

    name, item_exists, item_index = f_misc_functions.lookup(
        'service', cfg.SERVICES)
    if item_exists is True:
        if f_misc_functions.verification() == 'y':
            del cfg.SERVICES[name]
            f_misc_functions.save_database()
    else:
        f_misc_functions.alert(
            "%s does not exist in the database." % name.title())

    menu_main.execute_menu('s')


def edit_price():
    pass
