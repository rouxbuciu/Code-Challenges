import os
import cfg
import fr_classes
import time
import fr_functions
import menu_main

# =========================
#       PROJECTS
# =========================


def view_projects(name, item_index):
    os.system("clear")

    print("\n\nDate".ljust(15) + "Project Name".ljust(50) + "Sessions")
    print("="*75)
    for item in cfg.CLIENT_LIST[item_index].projects:
        print(item.date.ljust(15) + item.name.ljust(50),
              str(len(item.sessions)))
    print("\n\nPress [return] to go back to Project Management.")

    choice = input("")
    menu_main.projects_menu(name, item_index)


def add_project(name, item_index):
    os.system('clear')

    proj_name = input("\n\nEnter new project name:\n >> ").lower()
    date = time.strftime("%d/%m/%Y")
    cfg.CLIENT_LIST[item_index].projects.append(fr_classes.Project(
        proj_name, date))

    fr_functions.save_database()
    menu_main.projects_menu(name, item_index)


def edit_project(name, item_index):
    os.system("clear")

    print('\nPlease choose a project to add a session to:\n')
    print("      Project Name")
    print("    " + "=" * 50)
    count = 1
    for item in cfg.CLIENT_LIST[item_index].projects:
        print("[%s] " % count + item.name.ljust(50).title())
        count += 1
    print("\n")

    project_choice = fr_functions.check_if_number() - 1
    session_date = time.strftime("%d/%m/%Y")
    print ("How long was the session length?")
    session_length = fr_functions.check_if_number()
    while True:
        service_name, service_exists, service_index = fr_functions.lookup(
            "service", cfg.SERVICES)
        if service_exists is True:
            cost = cfg.SERVICES["%s" % service_name.title()] * session_length
            cfg.CLIENT_LIST[item_index].projects[
                project_choice].sessions.append(fr_classes.Sessions(
                    session_date, service_name, session_length, cost))
            break
        else:
            fr_functions.alert("Service does not exist.")

    fr_functions.save_database()
    menu_main.projects_menu(name, item_index)


def view_project_sessions(name, item_index):
    os.system("clear")

    print("\n\nWhich project's sessions would you like to view:\n")
    print("      Project Name")
    print("    " + "=" * 50)
    count = 1
    for item in cfg.CLIENT_LIST[item_index].projects:
        print("[%s] " % count + item.name.ljust(50).title())
        count += 1
    print("\n")
    project_choice = fr_functions.check_if_number() - 1

    os.system('clear')
    print("\n\nProject Name: %s\n" % cfg.CLIENT_LIST[item_index].projects[
          project_choice].name)
    print("Date".ljust(15) + "Session Service".ljust(20) + "Length     " +
          "Session Cost")
    print("="*70)
    for item in cfg.CLIENT_LIST[item_index].projects[project_choice].sessions:
        print(str(item.date).ljust(15) + item.service.ljust(20) +
              str(item.length).ljust(11) + str(item.cost))
    overall_project_cost = 0
    for item in cfg.CLIENT_LIST[item_index].projects[project_choice].sessions:
        overall_project_cost = overall_project_cost + item.cost
    print("\nProject charges: $%s" % overall_project_cost)
    print("\n\nPress [return] to go back to Project Management.")

    choice = input("")
    menu_main.projects_menu(name, item_index)
