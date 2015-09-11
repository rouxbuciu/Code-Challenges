import os
import menu_main
import fr_classes
import fr_functions
import cfg

# ===============================
#          CLIENT MENU
# ===============================


def add_client():
    os.system("clear")
    first_name = input("\n\nEnter client's first name:\n >> ").title()
    last_name = input("\nEnter client's last name:\n  >> ").title()
    kind = input("\nEnter customer type (band, company, artist, etc):\n >> ")
    email = input("\nEnter client e-mail:\n >> ").lower()
    phone = input("\nEnter client phone (###-###-####):\n >> ")
    street = input("\nEnter client's street address:\n >>")
    city = input("\nEnter client's city and province:\n >>").title()
    country = input("\nEnter client's country:\n >>")
    zipcode = input("\nEnter client's postal code:\n >>")
    survey = input("\nHow did client hear about us?\n >>").lower()

    os.system('clear')
    print("\n\nPlease review the information entered:")
    print("\n%s %s" % (first_name, last_name))
    print("Type: " + kind.title())
    print("Contact info: %s    %s" % (email, phone))
    print("\nAddress:")
    print(street)
    print(city, country)
    print(zipcode)
    print("Found studio through %s" % survey)
    if fr_functions.verification(False) == 'y':
        cfg.CLIENT_LIST.append(fr_classes.Client(first_name, last_name,
                               kind, email, phone, street, city, country,
                               zipcode, survey))
        fr_functions.save_database()

    menu_main.execute_menu('c')


def edit_client_info():
    os.system('clear')

    client_name, cilent_exists, client_index = fr_functions.lookup(
        "client's", cfg.CLIENT_LIST)

    print("\tCurrent client information:")
    print("\t" + item.first_name + " " + item.last_name)
    print("\t" + item.street)
    print("\t" + item.city)
    print("\t" + item.country)
    print("\t" + item.zipcode)
    print("\t" + item.email)
    print("\t" + item.phone)

    new_email = input("\n\tEnter client e-mail:\n >> ").lower()
    new_phone = input("\n\tEnter client phone (###-###-####):\n >> ")
    new_street = input("\n\tEnter client's street address:\n >>")
    new_city = input("\n\tEnter client's city and province:\n >>").title()
    new_country = input("\n\tEnter client's country:\n >>")
    new_zipcode = input("\n\tEnter client's postal code:\n >>")

    fr_functions.alert("Warning: you cannot undo this change.")
    if fr_functions.verification() == 'y':
        cfg.CLIENT_LIST[client_index].email = new_email
        cfg.CLIENT_LIST[client_index].phone = new_phone
        cfg.CLIENT_LIST[client_index].street = new_street
        cfg.CLIENT_LIST[client_index].city = new_city
        cfg.CLIENT_LIST[client_index].country = new_country
        cfg.CLIENT_LIST[client_index].zip_code = new_zipcode

    menu_main.execute_menu('c')


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
