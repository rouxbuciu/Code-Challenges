import sys
import os
import time
import pickle
import menu_client
import menu_main
import f_classes
import f_misc_functions
import cfg
import fandango_pos


def client_menu():
    os.system('clear')

    context_actions = {
        'v': menu_client.view_all_clients,
        'a': menu_client.add_client,
        'r': menu_client.remove_client,
    }

    print("Fandango Recording - The Business End\n")
    print("Client Management\n")
    print("[v] View All Clients")
    print("[a] Add Client")
    print("[r] Remove Client\n")
    choice = input(" >> ")
    execute_menu(choice, context_actions)
    return


def exit():
    f_misc_functions.save_database()
    sys.exit()


def execute_menu(choice, context_actions={"xyz": "It works."}):
    os.system('clear')
    ch = choice.lower()
    if ch == '':
        menu_actions['c']()
    else:
        try:
            if ch in context_actions:
                context_actions[ch]()
            else:
                menu_actions[ch]()
        except KeyError:
            print("Invalid selection, please try again.\n")
            menu_actions['c']()




# =============================
#          CONSTANTS
# =============================
menu_actions = {
    'c': client_menu,
    'q': exit,
}
