"""
Can you create a Program I will give you number(userinput and print table)

f"{}" String format concept
User input - num int -> 10, 100, -1, 2, 3.14 -> input
9x1 = 9
9x2 = 18... till 10
"""

number = float(input("Enter your number: "))

if number.is_integer():
    number = int(number)

# using f'{}' string
print(f'{number} * 1 = {number}')
print(f'{number} * 2 = {number*2}')
print(f'{number} * 3 = {number*3}')
print(f'{number} * 4 = {number*4}')
print(f'{number} * 5 = {number*5}')
print(f'{number} * 6 = {number*6}')
print(f'{number} * 7 = {number*7}')
print(f'{number} * 8 = {number*8}')
print(f'{number} * 9 = {number*9}')
print(f'{number} * 10 = {number*10}')
