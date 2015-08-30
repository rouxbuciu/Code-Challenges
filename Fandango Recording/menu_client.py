import os
import menu_main
import fr_classes
import fr_functions
import cfg
import menu_projects

# ===============================
#          CLIENT MENU
# ===============================


def add_client():
    os.system("clear")
    first_name = input("\n\nEnter client's first name:\n >> ").title()
    last_name = input("\nEnter client's last name: \n >> ").title()
    kind = input("\nEnter customer type (band, company, artist, etc):\n >> ")
    email = input("\nEnter client e-mail:\n >> ").lower()
    phone = input("\nEnter client phone (###-###-####):\n >> ")
    # client_id = f_classes.Client(first_name, last_name, kind, email, phone)

    os.system('clear')
    print("\n\nPlease review the information entered:")
    print("\n%s %s" % (first_name, last_name))
    print("Type: " + kind.title())
    print("Contact info: %s    %s" % (email, phone))
    if fr_functions.verification(False) == 'y':
        cfg.CLIENT_LIST.append(fr_classes.Client(first_name, last_name,
                               kind, email, phone))
        fr_functions.save_database()

    menu_main.execute_menu('c')


def remove_client():
    pass


def view_all_clients():
    os.system('clear')
    print("\n\nClient Name".ljust(27) + "projects  " +
        "phone".ljust(14) + "email")
    print("="*80)
    for client in cfg.CLIENT_LIST:
        name = client.first_name + " " + client.last_name
        print("| " + str(name).ljust(25) + str(
            len(client.projects)).ljust(7) + client.phone.ljust(15) +
            client.email)
    print("\n\nPress [return] to go back to Client Management.")

    choice = input("")
    menu_main.execute_menu('c')
