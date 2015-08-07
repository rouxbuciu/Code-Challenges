##How many test casese
##preparing to store the answer in a dictionary of lists
test_cases = int(raw_input("How many test cases: "))
answer = {}

##Loop for each test case
for n in range(0, test_cases):
    ##get the two times and turn them into integers
    time = raw_input("Data: ").split()
    time = map(int, time)

    ##turn each day into seconds since beginning of month
    ##find out the difference between the two
    ##convert the difference into a day, hour, minute, seconds value
    day1 = ((time[0] * 24 * 60 * 60) + (time[1] * 60 * 60)
        + (time[2] * 60) + time[3])
    day2 = ((time[4] * 24 * 60 * 60) + (time[5] * 60 * 60)
        + (time[6] * 60) + time[7])
    difference = day2 - day1
    seconds = difference % 60
    minutes = ((difference - seconds) / 60) % 60
    hours = (((difference - seconds) / 60) - minutes) / 60 % 24
    days = (((((difference - seconds) / 60) - minutes) / 60) - hours) / 24

    ##create bins recursively for each answer with the case number
    ## and the difference time
    answer[n+1] = [days, hours, minutes, seconds]

##print the answer on one line, with each case enclosed in ()
print ' '.join("(" + str(answer[n]).translate(None, '[],') + ")"
        for n in range(1, test_cases+1))
