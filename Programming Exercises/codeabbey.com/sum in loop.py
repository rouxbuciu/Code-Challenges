amount_of_values = int(raw_input("How many numbers?\n"))
values = raw_input("Enter numbers:\n").split(' ')
total = 0

for i in range(0, amount_of_values):
    total = total + int(values[i])

print total

#python alternative
ptotal = 0

for i in range(0, len(values)):
    ptotal = ptotal + int(values[i])

print ptotal
