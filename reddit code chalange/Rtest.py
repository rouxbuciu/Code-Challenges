y = 'abcde'
x = 'debta'

print x[1]

if x[1] in y:
    print "yes"
    print y.index(x[1])

if x[3] in y:
    print "yes"
else:
    print "no"
