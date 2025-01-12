### Ejercicio 1

def has_lucky_number(nums):
    """Return whether the given list of numbers is lucky. A lucky list contains
    at least one number divisible by 7.
    """
    for num in nums:
        if num % 7 == 0:
            return True
        else:
            return False
        
### Ejercicio 2

def elementwise_greater_than(L, thresh):
    """Return a list with the same length as L, where the value at index i is 
    True if L[i] is greater than thresh, and False otherwise.
    
    >>> elementwise_greater_than([1, 2, 3, 4], 2)
    [False, False, True, True]
    """
    greaters = []
    for num in L:
        if num > thresh:
            greaters.append(True)
        else:
            greaters.append(False)
    return greaters

# Aca hay una solución

# def elementwise_greater_than(L, thresh):
#     res = []
#     for ele in L:
#         res.append(ele > thresh)
#     return res
# Y aca está la solución con list comprehension

# def elementwise_greater_than(L, thresh):
#     return [ele > thresh for ele in L]


### Ejercicio 3

def menu_is_boring(meals):
    """Given a list of meals served over some period of time, return True if the
    same meal has ever been served two days in a row, and False otherwise.
    """
    for i in range(len(meals)-1):
        if meals[i] == meals[i+1]:
            return True
    return False
        
print(menu_is_boring(['Spam', 'Eggs', 'Spam', 'Spam', 'Bacon', 'Spam']))

print(help(range))


### Ejercicio 4

# Al lado de la mesa de blackjack, el desafío casino de Python tiene una maquina de slot.
# Puedes obtener un resultado de la maquina de slot llamando a play_slot_machine().
# El número que devuelve, es tu ganacia en dolares. Usualmente devuelve 0. 
# Pero a veces podes tener suerte y que devuelva una gran ganancia. Intenta correrlo aca abajo:

import random
def custom_random():
     # Valores posibles
    valores = [0, 1.5, 5]
    # Pesos: 99.8% para 0, 0.10% para 1.5, 0.10% para 5
    pesos = [80, 15, 5]
    # Seleccionar un valor basado en las probabilidades
    return random.choices(valores, weights=pesos, k=1)[0]
    
def play_slot_machine():
    return custom_random()

print(play_slot_machine())

def estimate_average_slot_payout(n_runs):
    # Play slot machine n_runs times, calculate payout of each
    payouts = [play_slot_machine()-1 for i in range(n_runs)]
    # Calculate the average value
    avg_payout = sum(payouts) / n_runs
    return avg_payout

print(estimate_average_slot_payout(1000))