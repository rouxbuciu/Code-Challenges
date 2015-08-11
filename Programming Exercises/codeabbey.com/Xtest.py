cases = {1: ["12", "34"], 2: ["56", "78"]}

print cases

for n in range(1, len(cases)+1):
    cases[n] = map(int, cases[n])

print cases
