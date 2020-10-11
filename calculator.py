#! /usr/bin/python3
# Calculator program that takes inputs from users and calculates the result

num1 = int(input('Enter the first number: '))
operator = input('Enter operator (+,-,/,*): ')
num2 = int(input('Enter the second number: '))

if operator == '+':
    result = num1 + num2
    print(result)
elif operator == '-':
    result = num1 - num2
    print(result)
elif operator == '/':
    if num2 == 0:
        print("Can't divide by 0")
    else:
        result = num1 / num2
        print(result)
elif operator == '*':
    result = num1 * num2
    print(result)



