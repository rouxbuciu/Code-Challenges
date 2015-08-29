print "Is this correct? (y/n)"
while True:
    verify = raw_input(" >> ").lower()
    try:
        if verify in ('y', 'n'):
            break
    except:
        print "Please enter a valid answer"

print verify
