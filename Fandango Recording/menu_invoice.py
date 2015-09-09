import os
import cfg
import fr_classes
import menu_projects
import fr_generate_invoice
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
    customer_info = [(cfg.CLIENT_LIST[client_index].last_name + "   " +
        cfg.CLIENT_LIST[client_index].first_name),
        cfg.CLIENT_LIST[client_index].phone,
        cfg.CLIENT_LIST[client_index].street,
        cfg.CLIENT_LIST[client_index].city,
        cfg.CLIENT_LIST[client_index].country,
        cfg.CLIENT_LIST[client_index].zip_code]
    invoice_date = time.strftime("%d/%m/%Y")
    invoice_number = fr_functions.find_invoice_number()

    os.system("clear")

    print("\n\nWhich project are you invoicing:\n")
    print("      Project Name")
    print("    " + "=" * 50)
    count = 1
    for item in cfg.CLIENT_LIST[client_index].projects:
        print("[%s] " % count + item.name.ljust(50).title())
        count += 1
    print("\n")
    project_choice = fr_functions.check_if_number() - 1

    services_rendered = []
    invoice_cost = 0

    while True:
        control_date = cfg.CLIENT_LIST[client_index].projects[
                project_choice].sessions[-1].date
        for item in cfg.CLIENT_LIST[client_index].projects[
                project_choice].sessions:
            if item.date == control_date:
                services_rendered.append(item)
                invoice_cost = invoice_cost + item.cost
        break

    cfg.INVOICES.append(fr_classes.Invoice(invoice_number, invoice_date,
                        invoice_cost, customer_info, services_rendered))
    current_invoice = cfg.INVOICES[-1]
    fr_functions.save_database()
    fr_functions.write_to_csv(fr_functions.unpack_invoice_information(
                              current_invoice))
    #fr_generate_invoice
    menu_main.main_menu()


def view_invoice():
    pass
