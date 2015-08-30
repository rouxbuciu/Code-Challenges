import os
import time
import pickle
import cfg

# ==============================
#       MISC FUNCTIONS
# ==============================


def save_database():
    with open("fandango database.txt", 'wb') as f:
        pickle.dump(cfg.CLIENT_LIST, f)

    with open("fandango services.txt", 'wb') as f:
        pickle.dump(cfg.SERVICES, f)


def alert(message=''):
    print("\n\n")
    print(message)
    time.sleep(2)


def check_if_number():
    while True:
        try:
            data = int(input(" >> "))
        except ValueError:
            print("Please enter a number.")
        else:
            break

    return data


# Checking with users if the information they entered is correct or if they
# are sure they want to proceed using a simple yes or no function
def verification(x=True):
    if x is True:
        os.system('clear')
        print("""




            ++++++++++++++++++++++++++++++++
            +                              +
            +        Are you sure?         +
            +           (y/n)              +
            +                              +
            +++++++++++++++++++++++++++++++=


        """)
    else:
        print("\nIs this correct? (y/n)\n")

    while True:
        verify = input(" >> ").lower()
        try:
            if verify in ('y', 'n'):
                break
        except:
            print("Please enter a valid answer.")
            time.sleep(1)
    return verify


# Useful function for checking whether a product name is in the productList
def lookup(search_term, search_array):
    while True:
        name = input("\nEnter %s name:\n >> " % search_term).title()
        if not search_array:
            item_exists = False
            item_index = None
            break
        else:
            for item in search_array:
                if search_array is cfg.SERVICES:
                    if name is item:
                        item_exists = True
                        item_index = None
                        break
                    else:
                        item_exists = False
                        item_index = None
                elif search_array is cfg.CLIENT_LIST:
                    if name is item.name:
                        item_exists = True
                        item_index = search_array.index(item)
                        break
                    else:
                        item_exists = False
                        item_index = None
            break
    return (name, item_exists, item_index)
