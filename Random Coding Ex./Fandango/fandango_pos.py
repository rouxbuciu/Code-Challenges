import sys
import os
import time
import pickle
import menu_services
import menu_actions
import menu_client
import menu_main
import f_classes
import menu_invoice
import f_misc_functions
import cfg
import fandango_pos
import projects

# ===========================================================================
# Fandango Client Point of Sale Project
#
# This software is a time keeping interface for charging clients based on the
# services they use and the time they spend in the studio.
# ===========================================================================

# =======================
#      MAIN PROGRAM
# =======================

# Before loading program, load the client daabase
try:
    with open('fandango database.txt', 'rb') as f:
        cfg.CLIENT_LIST = pickle.load(f)
except EOFError:
    pass

try:
    with open('fandango services.txt', 'rb') as f:
        cfg.SERVICES = pickle.load(f)
except EOFError:
    pass

# Main program
if __name__ == "__main__":
    menu_main.main_menu()
