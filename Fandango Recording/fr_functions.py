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

    with open("fandango_invoices.txt", 'wb') as f:
        pickle.dump(cfg.INVOICES, f)


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
                    if name == item:
                        item_exists = True
                        item_index = None
                        break
                    else:
                        item_exists = False
                        item_index = None
                elif search_array is cfg.CLIENT_LIST:
                    temp_name = item.first_name + " " + item.last_name
                    if name == temp_name:
                        item_exists = True
                        item_index = search_array.index(item)
                        break
                    else:
                        item_exists = False
                        item_index = None
            break
    return (name, item_exists, item_index)


def find_invoice_number():
    if not cfg.INVOICES:
        invoice_num = 1
    else:
        invoice_num = cfg.INVOICES[-1].invoice_number + 1

    return invoice_num


def write_to_csv(information):

    with open("fr_csv_data.csv", "w") as f:
        f.write(','.join(str(e) for e in information))


def unpack_invoice_information(invoice):
    invoice_information = []
    name = invoice.customer_info[0]
    street = invoice.customer_info[2]
    city = invoice.customer_info[3]
    country = invoice.customer_info[4]
    zip_code = invoice.customer_info[5]
    phone = invoice.customer_info[1]
    inv_date = invoice.invoice_date
    inv_number = str(invoice.invoice_number).zfill(5)
    total = invoice.total
    discount = invoice.discount
    final_total = invoice.final_total
    invoice_information = [name, street, city, country, zip_code,
                           phone, inv_date, inv_number, total, discount,
                           final_total]
    for item in invoice.services_rendered:
        invoice_information.append(item.service)
        invoice_information.append(item.length)
        invoice_information.append(item.cost)
        invoice_information.append(item.unit_price)
        invoice_information.append(item.date)

    return invoice_information
