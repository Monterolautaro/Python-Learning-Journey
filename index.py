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

### DESEMPAQUETADO MULTIPLE, O ASIGNACION SIMULTANEA
a, b, c = 1, 2, 3

print(a, b, c)

# Con listas
a = [1, 2, 3]
b = [4, 5, 6]

print("Antes del cambio", { "a": f"{a}", "b": f"{b}"})

a, b = b, a    # Se crea una tupla y se desempaqueta

# Primero python crea la tupla temporal:                      a, b = (b, a)
# Luego le asigna los respectivos valores a las variables:    a = b, b = a

print("Despues del cambio",{ "a": f"{a}", "b": f"{b}"})

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


# In the previous exercise, the candy-sharing friends Alice,
#  Bob and Carol tried to split candies evenly. For the sake of their friendship,
#  any candies left over would be smashed. For example, if they collectively bring
#  home 91 candies, they'll take 30 each and smash 1.

def to_smash(total_candies, friends_number = 3):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between the friends given, if no friends given,
    are set by default in three.
    
    >>> to_smash(91)
    1
    """
    if friends_number > 0:
        result = total_candies % friends_number
        return result

print(to_smash(90))
print(to_smash(91, 4)) 