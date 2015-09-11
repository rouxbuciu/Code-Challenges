import os
import cfg
import fr_classes
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
    customer_info = [(cfg.CLIENT_LIST[client_index].first_name + " " +
        cfg.CLIENT_LIST[client_index].last_name),
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

    print("Total invoice cost will be $%s." % invoice_cost)
    print("Current discount for invoice is: $0")
    if fr_functions.verification(False) == 'n':
        print("What discount would you like to offer (in CAD dollars)?")
        discount = fr_functions.check_if_number()
    else:
        discount = 0

    final_invoice_total = invoice_cost - discount

    cfg.INVOICES.append(fr_classes.Invoice(invoice_number, invoice_date,
                        invoice_cost, discount, final_invoice_total,
                        customer_info, services_rendered))
    current_invoice = cfg.INVOICES[-1]
    fr_functions.save_database()
    fr_functions.write_to_csv(fr_functions.unpack_invoice_information(
                              current_invoice))
    fr_generate_invoice.make_invoice()


def view_invoice():
    os.system('clear')

    print("\n\nTo find specific invoices, please enter client's full name:")
    name = input(" >> ").title()
    temp_list = []
    for item in cfg.INVOICES:
        if name == item.customer_info[0]:
            temp_list.append(item)
        elif name != item.customer_info[0] and item is cfg.INVOICES[-1] and (
                not temp_list):
            fr_functions.alert("No such customer exists.")
            menu_main.invoice_menu()

    os.system("clear")
    print("\n\n\tShowing past invoices for:")
    print("\t" + temp_list[1].customer_info[0])
    print("\t" + temp_list[1].customer_info[2])
    print("\t" + temp_list[1].customer_info[3])
    print("\t" + temp_list[1].customer_info[4])
    print("\t" + temp_list[1].customer_info[5])

    print("\n\n" + "Invoice No.".rjust(15) + "  Invoice Date")
    print("=" * 40)
    count = 1
    for item in temp_list:
        print(str(count).ljust(4) + str(
              item.invoice_number).rjust(11).zfill(5) + "  " +
              item.invoice_date)
        count += 1

    print("\nWhich invoice would you like to view:")
    view_invoice = fr_functions.check_if_number() - 1
    current_invoice = temp_list[view_invoice]
    fr_functions.write_to_csv(fr_functions.unpack_invoice_information(
                              current_invoice))
    fr_generate_invoice.make_invoice()
    menu_main.main_menu()
