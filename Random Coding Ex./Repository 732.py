##############################################################################
#
#           R732
#                   a simple game | ex35 of Learn Python the Hard Way
#                   feb 2015
#                   programmer | roux g buciu
#
#
#   CODE TABLE OF CONTENTS
#
#   1.  IMPORTS
#   2.  GLOBAL VARIABLES
#   3.  REPLAYABILITY
#   4.  GAME-STATE & BACKGROUND FUNCTIONS
#   5.  COMMANDS
#   6.  GAME LEVELS
#   7.  LEVEL LISTS
#   8.  SILLY-FRILLY GAME INTRO STUFF
#   9.  'READ' COMMAND ENTRIES
#   10. 'RUN' COMMAND ENTIRES
#   11. GAME KICKOFF - (I hate football. Why use a football metaphor?)
#
#
#           ~ COMMENTS ~
#
#   To Do
#   -Figure out why l3b2s2 closes
#       * (ie, why does l3b2s2_access change!?!?!)
#   -Read/Run functions make no sense as is
#       * (ie. Run -> [enter] -> enter file name
#       * cleanup can be "run uasf_prgm"
#       * will this create massive clutter in the commands()?
#   - Clean up the story. It was hastily written
#   - Document code well - in progress
#   - Add ValueError things to password inputs, etc.
#
##############################################################################
##############################################################################
# 1.    IMPORTS
##############################################################################

import random
from sys import exit
import os
import time


##############################################################################
# 2.    GLOBAL VARIABLES
##############################################################################

user_position = 0           # where player is
corruption_level = 5.0      # game main fail state
user_input = None           # no idea what this is for but its for something
secret_room_password = []   # creating a list for a randomly generated password
pass_gen = 'acoh.72mj2r8'   # random starting password to prevent cheating
user_pass = []              # for comparing generated password
l3b2s2_access = 0           # access to room l3b2s2 - off at start


##############################################################################
# 3.    REPLAYABILITY
##############################################################################

# a function that I will use to give the game replay value
# by giving different numbers each time the game is run
def replay(num):
    num = random.randrange(100, 999)
    return num

# Set the password and room access number for the secret room
for i in range(0, 3):
    secret_room_password.append(replay(pass_gen))

secret_room_locked = replay(pass_gen) ** 2
secret_room_unlocked = secret_room_locked + 1


##############################################################################
# 4.    GAME-STATE & BACKGROUND FUNCTIONS
##############################################################################

# here I check whether or not the user has figured out the password
# to access the secret room
def password_check(userpass, password, corruption_level):
    clear()
    print "This directory is password protected."
    for i in range(1, 4):
        userpass.append(int(raw_input(
            "\n\nEnter password sequence %d:\n>> " % i)))

    if password == userpass:
        where = secret_room_unlocked
        location(where, corruption_level, l3b2s2_access)
    else:
        print "Fatal data corrupiton."
        time.sleep(3)
        exit(0)

# corruption level increases every time the user performs a direct
# command: mfor, mbak, run, read
# when max corruption is reached, the game crashes and the user has to start
# again
def corrupt(arg):
    if arg >= 98.0:
        print """Corruption has reached critical levels.
Initiating fail-safe quarantine deletion protocols."""
        time.sleep(1)
        print "Critical failure."
        time.sleep(1)
        print "exit()"
        exit(0)
    elif arg == 50.0:
        print "**** Warning: file/system corruption at 50% ****"
        time.sleep(2)
        arg +=  2.5
        return float(arg)
    else:
        arg += 2.5
        return float(arg)

# used by various commands to move between levels
# it seemes unnecessarily complex but I've never done this before so
# I just can't really tell
def location(where, corruption_level, l3b2s2_access):
    if where == 0:
        start_menu()
    elif where == 1:
        l1(where, corruption_level, l3b2s2_access)
    elif where == secret_room_locked:
        l9closed(where, corruption_level, l3b2s2_access)
    elif where == secret_room_unlocked:
        l9open(where, corruption_level, l3b2s2_access)
    elif where == 10:
        l2b1(where, corruption_level, l3b2s2_access)
    elif where == 20:
        l2b2(where, corruption_level, l3b2s2_access)
    elif where == 11:
        l3b1s1(where, corruption_level, l3b2s2_access)
    elif where == 12:
        l3b1s2(where, corruption_level, l3b2s2_access)
    elif where == 13:
        l3b1s3(where, corruption_level, l3b2s2_access)
    elif where == 21:
        l3b2s1(where, corruption_level, l3b2s2_access)
    elif where == 22:
        l3b2s2(where, corruption_level, l3b2s2_access)
    else:                   # fucking jokes
        print """Never gonna give you up,
Never gonna let you down,
Never gonna run around and desert you."""

# clear the terminal screen -  keeping game real estate clean
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


##############################################################################
# 5.    COMMANDS
##############################################################################

# Here I will declare the game commands
def commands(choice, files, l3b2s2_access, corruption_level, where):
    if choice == "list":
        list_comm(where, corruption_level, l3b2s2_access)
    elif choice == "run":
        print "Enter _prgm to run."
        run_prgm = str(raw_input(">> "))
        run(run_prgm, where, corruption_level, l3b2s2_access)
    elif choice == "read":
        print "What _entry would you like to access:"
        read_entry = str(raw_input(">> "))
        read(read_entry, where, corruption_level)
    elif choice == "mfor":
        mfor(where, corruption_level, l3b2s2_access)
    elif choice == "mbak":
        mbak(where, corruption_level, l3b2s2_access)
    elif choice == "map":
        call_map()
        location(where, corruption_level, l3b2s2_access)
    elif choice == "corr":
        print "Corruption at %f%%." % corruption_level
        time.sleep(1.5)
        location(where, corruption_level, l3b2s2_access)
    elif choice == "help":
        console_help(where)
    elif choice == "quit":
        print "Logging out."
        time.sleep(1)
        exit(0)
    else:
        print "Unrecognized repository command."
        location(where, corruption_level, l3b2s2_access)

# The HELP command
def console_help(where):
    clear()
    print"""
Repository Command Help Module:

[list]      Lists available files in current repository level

[read]      Reads an available _entry file

[run]       Execute an available _prgm file

[mfor]      Move forwards a repository level

[mbak]      Move back a repository level

[map]       Display a map of the repository

[corr]      Check current file/system corrupiton level.

[quit]      Logoff from repository.

Type "help" at any time to bring up this help module.
Press [r] to return go back.
"""
    console_escape = raw_input(">> ")
    location(where, corruption_level, l3b2s2_access)

# the LIST command - listing files in fake directories
def list_comm(where, corruption_level, l3b2s2_access):
    if where == 1:
        l1_contents()
    elif where == secret_room_unlocked:
        l9open_contents()
    elif where == 10:
        l2b1_contents()
    elif where == 20:
        l2b2_contents()
    elif where == 11:
        l3b1s1_contents()
    elif where == 12:
        l3b1s2_contents()
    elif where == 13:
        l3b1s3_contents()
    elif where == 21:
        l3b2s1_contents()
    elif where == 22:
        l3b2s2_contents()
    else:
        print "Cthulhu is coming!"

    user_input = str(raw_input(">> "))
    commands(user_input, 1, l3b2s2_access, corruption_level, where)

# the RUN command - fake .exe type stuff
def run(passed_entry, where, corruption_level, l3b2s2_access):
    corruption_level = corrupt(corruption_level)
    if passed_entry == 'uasf_prgm' and where == 12:
        l3b2s2_access = uasf_prgm(l3b2s2_access)
        location(where, corruption_level, l3b2s2_access)
    elif passed_entry == 'portAccess_prgm' and where == secret_room_unlocked:
        portAccess_prgm()
    else:
        print "No such _prgm exists."
        time.sleep(1)
        location(where, corruption_level, l3b2s2_access)

# the READ command - because without reading there would be no programming
# or passwords for solving the game
def read(read_entry, where, corruption_level):
    corruption_level = corrupt(corruption_level)
    if read_entry == 'd001_entry' and where == 1:
        d001_entry()
    elif read_entry == 'd014_entry' and where == 1:
        d014_entry()
    elif read_entry == 'd035_entry' and where == 10:
        d035_entry()
    elif read_entry == 'd084_entry' and where == 10:
        d084_entry()
    elif read_entry == 'd028_entry' and where == 20:
        d028_entry()
    elif read_entry == 'd168_entry' and where == 13:
        d168_entry()
    elif read_entry == 'd238_entry' and where == 21:
        d238_entry()
    elif read_entry == 'd483_entry' and where == 21:
        d483_entry()
    elif read_entry == 'd504_entry' and where == 22:
        d504_entry()
    elif read_entry == 'd567_entry' and where == secret_room_unlocked:
        d567_entry()
    else:
        print "No such _entry exists."
        time.sleep(1)

    location(where, corruption_level, l3b2s2_access)

# the MFOR command - moving down a directory
def mfor(where, corruption_level, l3b2s2_access):
    clear()
    corruption_level = corrupt(corruption_level)
    if where == 1:
        print "What directory would you like to access:\n\n\n"
        print "Branch [1]"
        print "Branch [2]"
        branch = int(raw_input(">> "))
        if branch == 1:
            where = 10
            location(where, corruption_level, l3b2s2_access)
        elif branch == 2:
            where = 20
            location(where, corruption_level, l3b2s2_access)
        elif branch == secret_room_locked:
            where = secret_room_locked
            location(where, corruption_level, l3b2s2_access)
        else:
            print "That repository Branch does not exist."
            time.sleep(1)
            location(where, corruption_level, l3b2s2_access)
    elif where == 10:
        print "What directory would you like to access:\n\n\n"
        print "Subdirectory [1]"
        print "Subdirectory [2]"
        print "Subdirectory [3]"
        branch = int(raw_input(">> "))
        if branch == 1:
            where = 11
            location(where, corruption_level, l3b2s2_access)
        elif branch == 2:
            where = 12
            location(where, corruption_level, l3b2s2_access)
        elif branch == 3:
            where = 13
            location(where, corruption_level, l3b2s2_access)
        else:
            print "That repository Subdirectory does not exist."
            time.sleep(1)
            location(where, corruption_level, l3b2s2_access)
    elif where == 20:
        print "What directory would you like to access:\n\n\n"
        print "Subdirectory [1]"
        print "Subdirectory [2]"
        branch = int(raw_input(">> "))
        if branch == 1:
            where = 21
            location(where, corruption_level, l3b2s2_access)
        elif branch == 2:
            where = 22
            location(where, corruption_level, l3b2s2_access)
        else:
            print "That repository Subdirectory does not exist."
            time.sleep(1)
            location(where, corruption_level, l3b2s2_access)
    else:
        print "That repository Branch does not exist."
        time.sleep(1)
        location(where, corruption_level)

# the MBAK command - moving up a directory
def mbak(where, corruption_level, l3b2s2_access):
    corruption_level = corrupt(corruption_level)
    if where == 1:
        print "You are already in the home directory."
        time.sleep(1)
        location(where, corruption_level, l3b2s2_access)
    elif where == 10 or where == 20:
        where = 1
        location(where, corruption_level, l3b2s2_access)
    elif where == 11 or where == 12 or where == 13:
        where = 10
        location(where, corruption_level, l3b2s2_access)
    elif where == 21 or where == 22:
        where = 20
        location(where, corruption_level, l3b2s2_access)
    else:
        print "Chluhu calls."

# ITS A MAP!!1!
# da an any key to return thing. yay
def call_map():
    clear()
    print"""



Master Directory
-   Branch 1
|   -   Subdirectory 1
|   -   Subdirectory 2
|   -   Subdirectory 3
-   Branch 2
|   -   Subdirectory 1
|   -   Subdirectory 2
-   ******"""
    time.sleep(4)


##############################################################################
# 6.    GAME LEVELS
##############################################################################

# Here I will list the levels that comprise the game

def l1(where, corruption_level, l3b2s2_access):
    clear()
    print "Repository 732:Level1\n\n\n\n"
    where = 1
    user_input = str(raw_input(">> "))
    commands(user_input, 1, l3b2s2_access, corruption_level, where)
    return where

def l9closed(where, corruption_level, l3b2s2_access):
    clear()
    password_check(user_pass, secret_room_password, corruption_level)
    return where

def l9open(where, corruption_level, l3b2s2_access):
    clear()
    print "Repository 732:Level*\n\n\n\n"
    where = secret_room_unlocked
    user_input = str(raw_input(">> "))
    commands(user_input, 1, l3b2s2_access, corruption_level, where)
    return where

def l2b1(where, corruption_level, l3b2s2_access):
    clear()
    print "Repository 732:Level2:Branch1\n\n\n\n"
    where = 10
    user_input = str(raw_input(">> "))
    commands(user_input, 1, l3b2s2_access, corruption_level, where)
    return where

def l2b2(where, corruption_level, l3b2s2_access):
    clear()
    print "Repository 732:Level2:Branch2\n\n\n\n"
    where = 20
    user_input = str(raw_input(">> "))
    commands(user_input, 1, l3b2s2_access, corruption_level, where)
    return where

def l3b1s1(where, corruption_level, l3b2s2_access):
    clear()
    print "Repository 732:Level3:Branch1:Subdirectory1\n\n\n\n"
    where = 11
    user_input = str(raw_input(">> "))
    commands(user_input, 1, l3b2s2_access, corruption_level, where)
    return where

def l3b1s2(where, corruption_level, l3b2s2_access):
    clear()
    print "Repository 732:Level3:Branch1:Subdirectory2\n\n\n\n"
    where = 12
    user_input = str(raw_input(">> "))
    commands(user_input, 1, l3b2s2_access, corruption_level, where)
    return where

# this room cannot be accessed after a certain number of moves
# the user cannot get part of the password.
# uh-oh, user!

def l3b1s3(where, corruption_level, l3b2s2_access):
    if corruption_level < 22:
        clear()
        print "Repository 732:Level3:Branch1:Subdirectory3\n\n\n\n"
        where = 13
        user_input = str(raw_input(">> "))
        commands(user_input, 1, l3b2s2_access, corruption_level, where)
        return where
    else:
        print "Corruption level is over 22%."
        print "Files in this subdirectory have been irrepairably damaged."
        print "Subdirectory path is no longer accessible."
        time.sleep(3)
        l2b1(where, corruption_level, l3b2s2_access)

def l3b2s1(where, corruption_level, l3b2s2_access):
    clear()
    print "Repository 732:Level3:Branch2:Subdirectory1\n\n\n\n"
    where = 21
    user_input = str(raw_input(">> "))
    commands(user_input, 1, l3b2s2_access, corruption_level, where)
    return where

# this room is technically locked. Until it is unlocked.
# because that's how locks work

def l3b2s2(where, corruption_level, l3b2s2_access):
    if l3b2s2_access == 1:
        clear()
        print "Repository 732:Level3:Branch2:Subdirectory2\n\n\n\n"
        where = 22
        user_input = str(raw_input(">> "))
        commands(user_input, 1, l3b2s2_access, corruption_level, where)
        return where
    else:
        print "This subdirectory is currently locked."
        time.sleep(2)
        l2b2(where, corruption_level, l3b2s2_access)

##############################################################################
# 7.    LEVEL LISTS
##############################################################################

# Here we define what the user sees when he uses the "list" command

def l1_contents():
    clear()
    print "Repository 732:Level1\n\n\n\n"
    print "d001_entry"
    print "d014_entry"

def l9open_contents():
    clear()
    print "Repository 732:Level******\n\n\n\n"
    print "d567_entry"
    print "portAccess_prgm"

def l2b1_contents():
    clear()
    print "Repository 732:Level2:Branch1\n\n\n\n"
    print "d035_entry"
    print "d084_entry"        # contains the secret room number

def l2b2_contents():
    clear()
    print "Repository 732:Level2:Branch2\n\n\n\n"
    print "d028_entry"      # contains password bit 1

def l3b1s1_contents():
    clear()
    print "Repository 732:Level3:Branch1:Subdirectory1\n\n\n\n"
    print "This subdirectory is empty." # A trap to waste 2 moves!

def l3b1s2_contents():
    clear()
    print "Repository 732:Level3:Branch1:Subdirectory2\n\n\n\n"
    print "uasf_prgm"

def l3b1s3_contents():
    clear()
    print "Repository 732:Level3:Branch1:Subdirectory3\n\n\n\n"
    print "d168_entry"          # contains pass bit 2

def l3b2s1_contents():
    clear()
    print "Repository 732:Level3:Branch2:Subdirectory1\n\n\n\n"
    print "d238_entry"
    print "d483_entry"

def l3b2s2_contents():
    clear()
    print "Repository 732:Level3:Branch2:Subdirectory2\n\n\n\n"
    print "d504_entry"          # contains pass bit 3

##############################################################################
# 8.    SILLY-FRILLY INTRO STUFF
##############################################################################

# Pretending to be a real big boy game with intro and a menu and all!

def intro():                # Game Start Screen
    clear()
    print "\n\n\n\nrepository mainframe access terminal"
    intro_name = str(raw_input("\n\n\n\n\nlogin: "))
    intro_password = str(raw_input("password: "))
    print """Access granted to Clearance level 4 {Detective} Class account.


*****
{ADMIN} access notes:
-For the investigation regarding the disappearance of employee P42|92J-aX8
-Please do not run any _prgm to preserve files for later internal investigation

{LEGAL} access notes for {Detective} assigned to case:
-Please submit copies of all public reports to the LEGAL department
-No files may be copied to or from the server
    [Please manually write down any information deemed important]

Loading data from mainframe. Please wait...
"""
    time.sleep(20)
    user_position = 0
    repo_access()

def repo_access():          # First puzzle: solution is in the game name
    repository = None
    clear()
    print "\n\n\n\n\n\n\n\n\n"
    print "What Repository number would you like to access?"
    repository = raw_input(">> ")
    try:
        repository = int(repository)
    except ValueError:
        print "Repositories are numbered and do not contain alphanumeric characters."

    if repository == 732:
        intro_text()
        #start_menu()   # used to skip intro for faster debugging
    elif repository != 732 and isinstance(repository, int):
        print "Your account has not been cleared to access that repository."
        time.sleep(1)
        repo_access()
    else:
        time.sleep(1)
        repo_access()

def intro_text():               # it's like a video, but with text
    clear()

    print """Welcome to Repository 732

    This repository maintained by P42|92J-aX8
    Last entry date....""", time.sleep(3)
    print "File/system corruption detected."
    time.sleep(2)
    print "Automated file/system repairs commencing. ERROR."
    time.sleep(4)
    print """User access has triggered systemwide fail-safe quarantine protocols.
    ERROR: This repository does not exist in databank index."""
    time.sleep(1)
    print "Generating index.\nWorking...."
    time.sleep(6)
    print "Index generation failed. Repository 732 will be deleted once corruption"
    print "levels have reached critical contamination."
    print "Complete investigation before repository deletion."
    print "Corruption origin: Level3:Branch1:Subdirectory3."
    print "Corruption origin location will become unavailable at 23% corruption."
    time.sleep(9)

    start_menu()

def start_menu():               # the start menu
    clear()

    start_menu_choice = None

    print """






    [E]xplore repository
    [M]ap out repository
    [R]epository commands (help)
    [Q]uit

    [A]bout
    """

    while start_menu_choice == None:

        start_menu_choice = str(raw_input(">>  "))

        if start_menu_choice == "e" or start_menu_choice == "E":
            l1(user_position, corruption_level, l3b2s2_access)
        elif start_menu_choice == "M" or start_menu_choice == "m":
            call_map()
            start_menu()
        elif start_menu_choice == "r" or start_menu_choice == "R":
            console_help(user_position)
        elif start_menu_choice == "a" or start_menu_choice == "A":
            print """



    the repository mainframe has been created and maintained by

    roux g. buciu




    02 | 2015"""
            time.sleep(3)
            start_menu()
        elif start_menu_choice == "q" or start_menu_choice == "Q":
            print "Logging out."
            time.sleep(2)
            clear()
            exit(0)
        else:
            print "Please input a valid choice."
            time.sleep(1)
            start_menu()


##############################################################################
# 8.    'READ' ENTRIES
##############################################################################

# Story time. User will not get story in order. That's ok. It's like a puzzle.
# I LOVE PUZZLES!!!
# (not really)

def d001_entry():
    print """Name: John McCarthy
Employee ID: P42|92J-aX8
Time since memory serum administration: 12 hours

Entry begins:

I have been hired by The Company to work on a new project. Until today, the
details have been scarce, despite assurances that my particular skillset was
perfectly suited for the job. But after I signed the contract and was the
memory serum was injected (seems like they've perfected the tech and can now
delete all new memories since the serum injection cleanly), they revealed
everything. My god.

The plan is to upload a human mind. To completely digitize it. This would
bypass years of research on creating moral artificial intelligences. A human
mind, boosted by computing power and quantum processors controlling.... What?
Would there even be a limit? City management, security... Even space
exploration. We would ne longer have to waste the lives of our astronauts to
just get somewhere.

I've been set up in their Hong Kong compound. It's beautiful, certainly. But
I can't escape the feeling that I'll come to view this as a prison. Cannot
leave till the project is finished. Patent protection.
"""
    move_on = raw_input("Hit any key to continue.")

def d014_entry():
    print """Name: John McCarthy
Employee ID: P42|92J-aX8
Time since memory serum administration: 14 days

Entry begins:

It's been two weeks now. The work is exciting, it's revolutionary. There's a
feeling of electric anticipation in the lab. And the caliber of my colleagues!
If's there's a team that has a chance to succeed in this endeavour, this is it!

What progress we've made is exciting, despite knowing that we haven't even
really begun the real work yet.

It hasn't been long now, but I miss my wife. After this project, we will never
have to be apart again.
"""
    move_on = raw_input("Hit any key to continue.")

def d035_entry():
    print """Name: John McCarthy
Employee ID: P42|92J-aX8
Time since memory serum administration: 35 days

Entry begins:

The compound is strange. The room across the hall... I've never seen anyone come
or go but at night I hear strange sounds coming from there. I've asked about
it but was very politely told to mind my owm business. I'll investigate later.

Project is on track. Better even than expected.
"""
    move_on = raw_input("Hit any key to continue.")

def d084_entry():
    print """Name: John McCarthy
Employee ID: P42|92J-aX8
Time since memory serum administration: 84 days

Entry begins:

The Company has provided us with a quantum based supercomputer.



We are going to upload and digitize a mouses' brain.







I've created a hidden repository: %d""" % secret_room_locked
    move_on = raw_input("Hit any key to continue.")

def d028_entry():
    print """Name: John McCarthy
Employee ID: P42|92J-aX8
Time since memory serum administration: 28 days

Entry begins:

No real breakthroughs. But that's a good sign. The project plan I've developed
requires little steps, consistently, rather than large, slow discoveries. The
Company is constantly sending a man named Mr. Ushi. It means bull. I wonder if
his parents knew what type of man he was going to be and named him so as a
warning or if he became so bullish from being called that all his life.

I called home and my wife is well. The caretaker said everythind is in order.

I've managed to create an encryption protocol. I've set aside a secret, locked
repository on the server that The Company's drones cannot detect. The first
part of the unlock code: %d""" % secret_room_password[0]

    move_on = raw_input("Hit any key to continue.")

def d168_entry():
    print """Name: John McCarthy
Employee ID: P42|92J-aX8
Time since memory serum administration: 168 days

Entry begins:

It has been....

We've managed to create a fully functional chimp upload. Everyone's excited.
Myself most of all. This means that soon... I almost can't even think about
seeing my wife again or I will be overcome with emotion.

The room across the hall. I've created a reverse lens and have been sneaking
looks inside through the peephole. The room is furnished just like mine. But
there's a whiteout pale, naked woman kneeling in the corner. Facing away from
the door. Always. And at night, I hear a scratching on the other side.

Also.... the room has no number on the door. But the way the doors are layed
out, its clear that it should be room %d.""" % secret_room_password[1]
    move_on = raw_input("Hit any key to continue.")

def d238_entry():
    print """Name: John McCarthy
Employee ID: P42|92J-aX8
Time since memory serum administration: 238 days

Entry begins:

I'm responsible. I pushed too hard. Our first human test subject died. The
second lost his mind....


A few days ago, I was looking into the rooms' peephole. All I saw was red. Like
a red paper had been used to cover up the peephole.

Now, all I see is red in my dreams.
"""
    move_on = raw_input("Hit any key to continue.")

def d483_entry():
    print """Name: John McCarthy
Employee ID: P42|92J-aX8
Time since memory serum administration: 483 days

Entry begins:

Mr. Ushi cornered me. He seemed out of sorts. He pushed me agaist the wall and
hit me in the stomach. He said it was for the cameras. He told me what was in
the room. A failed experiment. A woman who was meant to seduce with phermones.
To distract. But it almost killed her. Now she has pale white skin and red eye
with no pupils.

I can't get her eyes out of my mind. I can't concentrate on my work well.
"""
    move_on = raw_input("Hit any key to continue.")

def d504_entry():
    print """Name: John McCarthy
Employee ID: P42|92J-aX8
Time since memory serum administration: 504 days

Entry begins:

The project is almost complete. Human mind digitization is now possible. We're
merely working on containment. New quantum/brain model has arrived. The power
this thing has is unbelievable.

Haven't seen Mr. Ushi for a long time.

Final code segment: %d.""" % secret_room_password[2]
    move_on = raw_input("Hit any key to continue.")

def d567_entry():
    print """Name: John McCarthy
Employee ID: P42|92J-aX8
Time since memory serum administration: 567 days

Entry begins:

The Company didn't tell me. My wife is dead. Power outage. And the caretaker
couldn't restart her life support and biostasys systems. I was too late. I
wasn't able to upload her.

The Company will pay for this.

If you're reading this, you must be investigating my disappearance. The Company
wouldn't have bothered even looking through this hidden directory. I'm going to
upload myself. I can cover my tracks. No-one will even know I am hidden in the
mainframe. I will be a ghost in the machine. I just won't be able to open access
to the internet or I'd be caught. Run the _prgm in this directory. Let me get
my revenge.
"""
    move_on = raw_input("Hit any key to continue.")


##############################################################################
# 9.    'RUN' ENTRIES
##############################################################################

# Here we 'run' the "run" command programs
# programs within programs... am I gonna be the father of the MATRIX?!

# unlocks l3b2s2
def uasf_prgm(arg):
    arg = 1
    print "Granting access to Level3:Branch2:Subdirectory2..."
    time.sleep(2)
    print "Access granted for 30 seconds."
    time.sleep(5)
    return arg

# This is the final choice in the game. If the user read everything
# it's supposed to have some meaning
def portAccess_prgm():
    clear()
    print "Would you like to enable Internet access to repository mainframe?"
    print "\n\n\n [Y]es / [N]o"
    final_choice = str(raw_input(">> "))
    if final_choice == 'Y' or final_choice == 'y':
        clear()
        print "Opening port access for repository mainframe."
        time.sleep(1)
        print "Open."
        time.sleep(1)
        print "[ANOMALY DETECTED]"
        print "Fail-safe overriden."
        print "Upload of [ANOMALY] commencing."
        time.sleep(2)
        exit(0)
    elif final_choice == 'N' or final_choice == 'n':
        clear()
        print "No changes made to reposi.(*&AOu!@*^ [ANOMALY DETECTED]"
        time.sleep(1)
        clear()
        print "\n\n\n\n\n\n\n\nI will find you."
        time.sleep(3)
        exit(0)
    else:
        print "Please enter a valid choice."
        time.sleep(1)
        portAccess_prgm()


##############################################################################
# 10.   GAME KICKOFF
##############################################################################

# let's play a game.
intro()
