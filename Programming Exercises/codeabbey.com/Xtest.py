au = {"1": 0, "2": 2}

print au

au["2"] = au["2"] + 1

print au["2"]
for n in range(1, len(au)+1):
    print str(au[str(n)]) + " text "
