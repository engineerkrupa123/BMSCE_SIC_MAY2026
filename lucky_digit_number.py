import pdb
pdb.set_trace()

input_number = int(input('Enter a number to find your lucky digit: '))
print(f'Number you input is {input_number}')

sum_of_digits = 0
while input_number != 0:
    remainder = input_number % 10
    input_number = input_number // 10
    sum_of_digits += remainder
    if sum_of_digits > 9 and input_number == 0:
        input_number = sum_of_digits
        sum_of_digits = 0

print('Your lucky digit is ', sum_of_digits)