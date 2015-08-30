import os
import menu_main
import fr_functions
import cfg

# =================================
#        SERVICES MENU
# =================================


def view_services():
    os.system('clear')
    print("\n\nService".ljust(40) + "  Price")
    print("="*60)
    for n in cfg.SERVICES:
        print("| " + str(n).ljust(38) + "| " + str(cfg.SERVICES[n]))
    print("\n\nPress [return] to go back to Services Management.")

    choice = input("")
    menu_main.execute_menu('s')


def add_service():
    new_service = input("\n\nEnter a service to add:\n\n >> ").title()
    print("\nHow much does this cost per hour?\n\n")
    cfg.SERVICES[new_service] = fr_functions.check_if_number()

    fr_functions.save_database()
    menu_main.execute_menu('s')


def remove_service():
    os.system('clear')
    print("\n\nServices currently offered:\n")
    for n in cfg.SERVICES:
        print(n)
    print("""
          *** WARNING ***
          Removing a service deletes it permanently from the database.""")

    name, item_exists, item_index = fr_functions.lookup(
        'service', cfg.SERVICES)
    if item_exists is True:
        if fr_functions.verification() == 'y':
            del cfg.SERVICES[name]
            fr_functions.save_database()
    else:
        fr_functions.alert(
            "%s does not exist in the database." % name.title())

    fr_functions.save_database()
    menu_main.execute_menu('s')


def edit_price():
    os.system('clear')
    while True:
        name, item_exists, item_index = fr_functions.lookup(
            'service', cfg.SERVICES)
        if item_exists is True:
            print("\nEnter new price per hour for %s." % name)
            cfg.SERVICES[name] = fr_functions.check_if_number()
            break
        else:
            fr_functions.alert(
                "%s does not exist in current Services database." % name)
            break

    fr_functions.save_database()
    menu_main.execute_menu('s')
