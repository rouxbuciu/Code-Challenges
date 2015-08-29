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


def main_menu():
    os.system('clear')

    print("Fandango Recording - The Business End\n")
    print("Main Menu\n")
    print("[c] Client Management")
    print("[s] Service Management")
    print("[i] Generate Invoice\n")
    print("[a] About\n")
    print("[q] Save & Quit")
    choice = input(" >> ")
    execute_menu(choice)
    return


def client_menu():
    os.system('clear')

    context_actions = {
        'v': menu_client.view_all_clients,
        'a': menu_client.add_client,
        'r': menu_client.remove_client,
        'm': projects_menu,
    }

    print("Fandango Recording - The Business End\n")
    print("Client Management\n")
    print("[m] Manage Client Projects")
    print("[v] View All Clients")
    print("[a] Add Client")
    print("[r] Remove Client\n")
    print("[b] Back\n")
    choice = input(" >> ")
    execute_menu(choice, context_actions)
    return


def projects_menu():
    pass


def invoice_menu():
    os.system('clear')

    print("Fandango Recording - The Business End\n")
    print("Invoices Menu\n")
    print("[p] Prepare Client Invoice\n")
    print("[b] back\n")
    choice = input(" >> ")
    execute_menu(choice)
    return


def service_menu():
    os.system('clear')

    context_actions = {
        'v': menu_services.view_services,
        'a': menu_services.add_service,
        'r': menu_services.remove_service,
        's': menu_services.edit_price,
    }

    print("Fandango Recording - The Business End\n")
    print("Services Management\n")
    print("[v] View Services Info")
    print("[a] Add Service")
    print("[r] Remove Service")
    print("[s] Service Price Management\n")
    print("[b] Back\n")
    choice = input(" >> ")
    execute_menu(choice, context_actions)
    return


def about_menu():
    os.system('clear')

    print("\n\n Fandango Recording - The Business End\n")
    print("\t\t\tv0.1\n")
    print("\tDesign & Code")
    print("\tRoux G. Buciu")
    print("\n\n\t(c) 2015")
    choice = input("")
    execute_menu(choice)
    return


def back_a_menu():
    menu_actions['main_menu']()


def exit():
    f_misc_functions.save_database()
    sys.exit()


def execute_menu(choice, context_actions={"xyz": "It works."}):
    os.system('clear')
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            if ch in context_actions:
                context_actions[ch]()
            else:
                menu_actions[ch]()
        except KeyError:
            print("Invalid selection, please try again.\n")
            menu_actions['main_menu']()




# =============================
#          CONSTANTS
# =============================
menu_actions = {
    'main_menu': main_menu,
    'c': client_menu,
    'a': about_menu,
    'b': back_a_menu,
    'i': invoice_menu,
    's': service_menu,
    'q': exit,
}
