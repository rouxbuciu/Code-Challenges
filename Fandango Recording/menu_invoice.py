import os
import cfg
import fr_classes
import fr_functions
import menu_main
import time

# ============================
#       INVOICE MENU
# ============================


def new_invoice():
    os.system('clear')
    client_name, client_exists, client_index = fr_functions.lookup(
        "client's", cfg.CLIENT_LIST)
    customer_info = [(cfg.CLIENT_LIST[client_index].last_name + ", " +
        cfg.CLIENT_LIST[client_index].first_name),
        cfg.CLIENT_LIST[client_index].email,
        cfg.CLIENT_LIST[client_index].phone,
        cfg.CLIENT_LIST[client_index].street,
        cfg.CLIENT_LIST[client_index].city,
        cfg.CLIENT_LIST[client_index].country,
        cfg.CLIENT_LIST[client_index].zip_code,
        cfg.CLIENT_LIST[client_index].kind]
    invoice_date = time.strftime("%d/%m/%Y")
    invoice_number = fr_functions.find_invoice_number()
    fr_functions.alert(customer_info)
    fr_functions.alert(invoice_number)
    #cfg.INVOICES.append(fr_classes.Invoice(invoice_number, invoice_date,
    #                    ))

    #fr_functions.save_database()
    #menu_main.main_menu()


def view_invoice():
    pass
