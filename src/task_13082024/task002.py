"""
Create a program , take 2 inputs from the user num1, num2 and give them
max
pow num1 to num2
sub, mul, sum, div.
Format your out with f'{}'
"""

num_1 = int(input("Enter your first number: "))
num_2 = int(input("Enter your second number: "))

# Max of two numbers
max_result = max(num_1, num_2)
print(f'The maximum of the two numbers is: {max_result}')

# Power of two numbers
pow_result = pow(num_1, num_2)
print(f'The result of the two numbers is: {pow_result}')

# Addition of two numbers
add_result = num_1 + num_2
print(f'The addition of the two numbers is: {add_result}')

# Subtraction of two numbers
sub_result = num_1 - num_2
print(f'The Subtraction of the two numbers is: {sub_result}')

# Multiplication of two numbers
mul_result = num_1 * num_2
print(f'The Multiplication of the two numbers is: {mul_result}')

# Division of two numbers (both quotient & remainder)
div_result = divmod(num_1, num_2)
print(f'The Division(Quotient, Remainder) of the two numbers is: {div_result}')

# Division of two numbers (quotient result only)
quot_result = num_1 / num_2
print(f'The Quotient of the two numbers is: {quot_result}')

# Division of two numbers without any decimals (quotient result only)
floordiv_result = num_1 // num_2
print(f'The Floor Division of the two numbers is: {floordiv_result}')

# Division of two numbers (Remainder result only)
remain_result = num_1 % num_2
print(f'The Remainder of the two numbers is: {remain_result}')
