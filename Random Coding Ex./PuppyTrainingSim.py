## A puppy training simulator to learn how to use classes.

## Imports
from random import randint
import time

## Creating a class that governs how obediance operates
class Training(object):

    def __init__(self):
        self.obedience = 1
        self.all_commands = 0

    def performance_level(self):
        if self.obedience >= 1 and self.obedience <= 3:
            self.all_commands = 1
        elif self.obedience >= 4 and self.obedience <= 6:
            self.all_commands = 2
        elif self.obedience >= 7 and self.obedience <= 9:
            self.all_commands = 3
        elif self.obedience >= 10:
            self.all_commands = 4

## Creating a chance that the puppy doesn't obey. The lower his obedience
## level, the greater the chance that he doesn't obey.
    def obey(self):
        if self.obedience >= 1 and self.obedience <= 3:
            chance = randint(1, 3)
        elif self.obedience >= 4 and self.obedience <= 6:
            chance = randint(1, 2)
        elif self.obedience >= 7 and self.obedience <= 9:
            chance = 1

        return chance

## Creating the puppy class that inherits Training traits
class Puppy(Training):

    def __init__(self, name):
        super(Puppy, self).__init__()
        self.name = name

    def positive_reward(self):
        self.obedience += 1

    def negative_reward(self):
        if self.obedience > 1:
            self.obedience -= 1
        else:
            pass

## Here, we can find the functions that define the commands that the puppy can
## do. They are each dependent on how obedient the puppy is, along with the
## chance that he doesn't obey from the obey() function.
    def sit(self):
        print "%s sits nicely, but excitedly, at your feet!" % self.name

    def lay_down(self):
        print "%s lays down, looking up, hoping for a treat!" % self.name

    def bark(self):
        if self.obedience >=4:
            print "%s barks a couple of times!" % self.name
        else:
            print "%s can't do that yet" % self.name

    def high_five(self):
        if self.obedience >=4:
            print "%s paws at you with his right paw!" % self.name
        else:
            print "%s can't do that yet" % self.name

    def play_dead(self):
        if self.obedience >=7:
            print "%s rolls onto his back and stays motionless!" % self.name
        else:
            print "%s can't do that yet" % self.name

## Here I'm checking whether the puppy obeyed the command and if he did, then
## increasing the obedience level. Alternatively, if he didn't obey, then
## we lower its obedience level.
    def give_a_treat(self, pup_listen):
        if pup_listen == 1:
            pup.positive_reward()
        elif pup_listen == 0:
            pup.negative_reward()

def command(pup_listen, user_command, p_command):

    if user_command == 'sit':
        chances = pup.obey()
        if chances == 1:
            pup.sit()
            pup_listen = 1
            return pup_listen
        else:
            print """
%s looks at you excitedly, cocking his head, and ignores your command.""" % (
        pup.name)
            pup_listen = 0
            return pup_listen

    elif user_command == 'lay down':
        chances = pup.obey()
        if chances == 1:
            pup.lay_down()
            pup_listen = 1
            return pup_listen
        else:
            print """
%s looks at you excitedly, cocking his head, and ignores your command.""" % (
        pup.name)
            pup_listen = 0
            return pup_listen

    elif user_command == 'bark':
        chances = pup.obey()
        if chances == 1:
            pup.bark()
            pup_listen = 1
            return pup_listen
        else:
            print """
%s looks at you excitedly, cocking his head, and ignores your command.""" % (
        pup.name)
            pup_listen = 0
            return pup_listen

    elif user_command == 'high five':
        chances = pup.obey()
        if chances == 1:
            pup.high_five()
            pup_listen = 1
            return pup_listen
        else:
            print """
%s looks at you excitedly, cocking his head, and ignores your command.""" % (
        pup.name)
            pup_listen = 0
            return pup_listen

    elif user_command == 'play dead':
        chances = pup.obey()
        if chances == 1:
            pup.play_dead()
            pup_listen = 1
            return pup_listen
        else:
            print """
%s looks at you excitedly, cocking his head, and ignores your command.""" % (
        pup.name)
            pup_listen = 0
            return pup_listen

    elif user_command == 'treat':
        if p_command != 'treat':
            pup.give_a_treat(pup_listen)
        else:
            print "You've already given %s a treat." % pup.name

        return pup_listen

    else:
        print "That's not a valid command."


def intro():
    print """
Welcome to the Puppy Training Simulation! Here, you get a chance to train your
puppy to obey some simple commands: SIT, LAY DOWN, BARK, HIGH FIVE,
and PLAY DEAD. There's three levels of obedience and your job is to get
your puppy to be able to perform all the commands. To pass the course, you must
get your puppy to perform each command at least once!

How to train your puppy: give him a command, for example, "sit". If he sits,
then give him a TREAT to encourage good bedaviour, or he won't learn and
progress in his training! But be warned: if you give him treats when he
doesn't listen, you'll be encouraging bad behaviour!

Let's go!
"""

## Now we start the game! First, the intro.
intro()

## Then, we find out what the pet's name is and create an instance
## of the puppy class with that name.

pup = raw_input("What is your puppy's name? ")
pup = Puppy(pup)
user_command = ' '
did_pup_listen = 9
prev_command = 'spud'

while pup.all_commands < 4:

    print "\n\n%s looks up at you, waiting for a command or a treat." % (
            pup.name)
    user_command = raw_input("")
    ## Taking user commands.
    did_pup_listen = command(did_pup_listen, user_command, prev_command)
    prev_command = user_command

    pup.performance_level()
    print "Obedience: %s/10" % pup.obedience
    print prev_command
    time.sleep(1)

print "Congratulations! You've trained %s well enough to pass the course!" % (
        pup.name)
