import sys
import os
import time
import pickle
import menu_client
import menu_main
import f_classes
import f_misc_functions
import cfg
import fandango_pos


# =======================
#      MAIN PROGRAM
# =======================

# Before loading program, load the client daabase
try:
    with open('fandango database.txt', 'rb') as f:
        cfg.CLIENT_LIST = pickle.load(f)
except EOFError:
    pass


# Main program
if __name__ == "__main__":
    menu_main.client_menu()
