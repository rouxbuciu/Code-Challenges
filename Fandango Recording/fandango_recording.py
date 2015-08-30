import pickle
import menu_main
import cfg


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
