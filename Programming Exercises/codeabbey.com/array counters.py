m_and_n = raw_input("Enter array length and 'n': ").split()

counter = {}
answer = []

for i in range(1, (int(m_and_n[1])+1)):
    counter["%s" % i] = 0

data = raw_input("Enter the data: ").split()

for i in range(0, int(m_and_n[0])):
    for n in range(1, (int(m_and_n[1])+1)):

        if int(data[i]) == n:
            counter["%s" % n] = counter["%s" % n] + 1

for n in range(1, (int(m_and_n[1]) + 1)):
    print str(counter[n])+" "
