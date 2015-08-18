##############################################################################
#
# r/dailyprogrammer C.228 [Easy] Letters in Alphabetical Order
#
# A handful of words have their letters in alphabetical order, that is nowhere
# in the word do you change direction in the word if you were to scan along the
# English alphabet. An example is the word "almost", which has its letters in
# alphabetical order.
#
# Your challenge today is to write a program that can determine if the letters
# in a word are in alphabetical order.
# As a bonus, see if you can find words spelled in reverse alphebatical order.
#
##############################################################################

def alph_check(word):
    word = list(word)
    if word == sorted(word):
        return "IN ORDER"
    elif word == sorted(word, reverse = True):
        return "REVERSE ORDER"
    else:
        return "NOT IN ORDER"

data = ['billowy', 'biopsy', 'chinos', 'defaced', 'chintz', 'sponged',
'bijoux', 'abhors', 'fiddle', 'begins', 'chimps', 'wronged']

for n in data:
    print n + " " + alph_check(n)
