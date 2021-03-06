# Each new term in the Fibonacci sequence is generated by adding the
# previous two terms. By starting with 1 and 2, the first 10 terms will be:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values do not
# exceed four million, find the sum of the even-valued terms.

even_valued_terms = 0
pcounter = 1
scounter = 1
tcounter = 1
f_list = []

while pcounter < 4000000:
    if pcounter % 2 == 0:
        even_valued_terms = even_valued_terms + pcounter

    tcounter = scounter
    scounter = pcounter
    pcounter = pcounter + tcounter
    f_list.append(pcounter)

print f_list
print even_valued_terms
