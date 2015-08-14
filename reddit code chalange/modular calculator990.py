## A different take on trying to do a weird mod calc
## mostly ignorable. It was from misunderstanding what a problem wanted

data_numbers = [int(raw_input("Enter initial integer: "))]
data_sign_value = ['+']
modulo_value = 0
data_entry_check_counter = 0
multiplication_checker = True

while True:
    sign, num = raw_input("Enter operational data: ").split()

    if sign == '%':
        modulo_value = int(num)
        break
    else:
        data_entry_check_counter += 1
        data_sign_value.append(sign)
        data_numbers.append(int(num))

while multiplication_checker == True:

    for n in range(0, len(data_sign_value)):

        if data_sign_value[n] == '*':
            result = (data_numbers[n] * data_numbers[n-1]) % modulo_value
            data_numbers[n-1] = result
            data_numbers.pop(n)
            data_sign_value.pop(n)
            break

    for n in range(0, len(data_sign_value)):

        if data_sign_value[n] == '*' and n <= (len(data_sign_value)-1):
           break
        elif n == (len(data_sign_value)-1) and data_sign_value[n] == "+":
            multiplication_checker = False

result = 0

for n in range(0, len(data_numbers)):
    result = result + data_numbers[n]

result = result % modulo_value

print result
