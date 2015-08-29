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
#           CLASSES
# ==============================


class Client(object):

    def __init__(self, first_name, last_name, kind, email, phone, projects=[]):
        self.first_name = first_name
        self.last_name = last_name
        self.kind = kind
        self.email = email
        self.phone = phone
        self.projects = projects
