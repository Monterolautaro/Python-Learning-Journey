amounts = 0

amounts = 1 + amounts

if amounts == 0:
    print("Hello")
    print("World")
    print('!')

else: 
    print("Bye")
    print("World")

amounts = "Soy yo "

print(amounts * 3)

# amounts = 0.45
print(type(amounts))

prueba = 1
print(type(prueba))

a = 3
b = 9

print(a % b) # 3

print(3 ** 2) # 9

print(3 / 2) # 1.5

## División que se redondea al entero mas cercano
print(3 // 2) # 1

print(7 // 3)

help(print)

def add(a, b, c):
    """return the maximum of three sums of 3 numbers (a, b, c)
    >>> add(1, 2, 3)
    6
    """
    one = a + c
    two = a + b
    three = a + b + c
    return max(one, two, three)

print(add(1, 2, 3))

help(add)


def least_difference(a, b, c):
    """Return the smallest difference between any two numbers
    among a, b and c.
    
    >>> least_difference(1, 5, -5)
    4
    """
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)

print(least_difference(1, 2, 3))

help(least_difference)


# ROUND NUMBERS WITH NEGATIVE SECOND ARGUMENT 

def tries_rounded_numbers(num):
    round_number1 = round(num, -1)
    round_number2 = round(num, -2)
    round_number3 = round(num, -3)
    round_number_positive3 = round(num, 3)
    # print({round_number1, round_number2})
    print([{"Number 1"},{round_number1}])
    print([{"Number 2"},{round_number2}])
    print([{"Number 3"},{round_number3}])
    print([{"Number positive"},{round_number_positive3}])
    return {round_number1, round_number2, round_number3}

# When you pass a -1, it will round to the nearest 10, for -2 to 100, for -3 to 1000, etc.
print(tries_rounded_numbers(2222.2333333))