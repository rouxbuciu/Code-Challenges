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

# ==============================
#       MISC FUNCTIONS
# ==============================


def save_database():
    with open("fandango database.txt", 'wb') as f:
        pickle.dump(cfg.CLIENT_LIST, f)
