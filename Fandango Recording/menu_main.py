import sys
import os
import menu_services
import menu_client
import menu_invoice
import cfg
import fr_functions
import menu_projects

# ============================================================================
#       MAIN MENU
#
# A text based menu where the user accesses the program's vairous functions.
# All links point to other program files. The only thing this file deos is
# manage the links between everything.
# ============================================================================


def main_menu():
    os.system('clear')

    print("\n\n\t\t\tHandle My Music Business\n")
    print("\tMain Menu\n")
    print("\t[c] Client Management")
    print("\t[s] Service Management")
    print("\t[u] Generate a Quote")
    print("\t[i] Generate Invoice\n")
    print("\t[a] About\n")
    print("\t[q] Save & Quit")
    choice = input("\n\t >> ")
    execute_menu(choice)
    return


def client_menu():
    os.system('clear')

    context_actions = {
        'v': menu_client.view_all_clients,
        'a': menu_client.add_client,
        'r': menu_client.remove_client,
        'm': pre_projects_menu,
    }

    print("\n\n\t\t\tHandle My Music Business\n")
    print("\tClient Management\n")
    print("\t[m] Manage Client Projects")
    print("\t[v] View All Clients")
    print("\t[a] Add Client\n")
    # print("\t[r] Remove Client\n")
    print("\t[b] Back\n")
    print("\t[q] Save & Quit")
    choice = input("\n\t >> ")
    execute_menu(choice, context_actions)
    return


def pre_projects_menu():
    os.system('clear')

    # Find out which client we are managing projects for and pass that
    # information to the actual projects menu
    name, item_exists, item_index = fr_functions.lookup(
        "client's full", cfg.CLIENT_LIST)

    if item_exists is True:
        projects_menu(name, item_index)
    else:
        fr_functions.alert("Client not found.")
        execute_menu('c')

    return


def projects_menu(name, item_index):
    os.system('clear')

    context_actions = {
        'v': menu_projects.view_projects,
        'p': menu_projects.view_project_sessions,
        'a': menu_projects.add_project,
        's': menu_projects.edit_project,
    }

    print("\n\n\t\t\tHandle My Music Business\n")
    print("\tProject Management for %s\n" % name)
    print("\t[v] View All Projects")
    print("\t[p] View Project Sessions")
    print("\t[a] Add a New Project")
    print("\t[s] Add a Session\n")
    print("\t[b] Back\n")
    print("\t[q] Save & Quit")
    choice = input("\n\t >> ")
    execute_menu(choice, context_actions, name, item_index)

    return


def invoice_menu():
    os.system('clear')

    print("\n\n\t\t\tHandle My Music Business\n")
    print("\tInvoices Menu\n")
    print("\t[p] Prepare Client Invoice\n")
    print("\t[b] back\n")
    print("\t[q] Save & Quit")
    choice = input("\n\t >> ")
    execute_menu(choice)
    return


def service_menu():
    os.system('clear')

    context_actions = {
        'v': menu_services.view_services,
        'a': menu_services.add_service,
        'r': menu_services.remove_service,
        'e': menu_services.edit_price,
    }

    print("\n\n\t\t\tHandle My Music Business\n")
    print("\tServices Management\n")
    print("\t[v] View Services Info")
    print("\t[a] Add Service")
    print("\t[r] Remove Service")
    print("\t[e] Edit Service Prices\n")
    print("\t[b] Back\n")
    print("\t[q] Save & Quit")
    choice = input("\n\t >> ")
    execute_menu(choice, context_actions)
    return


def quote_menu():
    pass

def about_menu():
    os.system('clear')

    print("\n\n\t\t\tHandle My Music Business\n")
    print("\t\t\tv0.1\n")
    print("\n\tClient ID: Fandango Recording Toronto\n\n")
    print("\tDesign & Code")
    print("\tRoux G. Buciu")
    print("\n\n\t(c) 2015 Roux Buciu")
    choice = input("")
    execute_menu(choice)
    return


def back_a_menu():
    menu_actions['main_menu']()


def exit():
    fr_functions.save_database()
    sys.exit()


def execute_menu(choice, context_actions={}, other=None, other2=None):
    os.system('clear')
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            if ch in context_actions and other != None:
                context_actions[ch](other, other2)
            elif ch in context_actions:
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
