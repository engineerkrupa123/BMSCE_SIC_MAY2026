input_number = int(input("Enter a number to find your lucky digit: "))

print(f"Number you input is {input_number}")

while input_number > 9:
    sum_of_digits = 0

    while input_number != 0:
        remainder = input_number % 10
        input_number = input_number // 10
        sum_of_digits += remainder

    input_number = sum_of_digits

print("Your lucky digit is:", input_number)

