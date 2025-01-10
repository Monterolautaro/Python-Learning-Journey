
# Primer ejercicio

# retornar el segundo elemento de la lista pasada como argumento
# Si la lista no tiene segundo elemento, retornar None
def select_second(L):
    """Return the second element of the given list. If the list has no second
    element, return None.
    """
    if not len(L) >= 2:
        return None
    else:
        return L[1]
    
# Segundo ejercicio   
    
# estas analizando equipos de deporte. Los miembros de cada uno de los equipos
# estan guardados en una lista. El Coach es el primer nombre en la lista, el capitan es el segundo
# nombre en la lista, y otros jugadores estan enlistados luego de ellos. Estas listas estan guardadas
# en otra lista, que empieza con el mejor equipo y procede en orden hasta el peor equipo al final.
# Completa la función de abajo para seleccionar al capitan del peor equipo.

def losing_team_captain(teams):
    """Given a list of teams, where each team is a list of names, return the 2nd player (captain)
    from the last listed team
    """
    captains_worst_team = teams[-1][1]
    return captains_worst_team


### Tercer ejercicio

# La siguiente iteración de Mario Kart va a incluir un nuevo item, la shell purpura.
# Cuando se usa, el corredor en el último lugar se teletransporta al primero, y el que 
# este en primer lugar se teletransporta al ultimo.
# Completa la función de abajo para implementar la shell purpura.
def purple_shell(racers):
    """Given a list of racers, set the first place racer (at the front of the list) to last
    place and vice versa.
    
    >>> r = ["Mario", "Bowser", "Luigi"]
    >>> purple_shell(r)
    >>> r
    ["Luigi", "Bowser", "Mario"]
    """
    racers[0], racers[-1] = racers[-1], racers[0]
    
    
    
### Cuarto ejercicio
    
# ¿Cual es la longitud de las siguientes listas? Rellena la varible lengths con
# tus predicciónes. (Sin usar len() en ellas.)
a = [1, 2, 3]
b = [1, [2, 3]]
c = []
d = [1, 2, 3][1:]

# Pon tus predicciones en la variable lengths. La logitud debería tener 4 numeros, el
# primero siendo la longitud de a, el segundo siendo la longitud de b y así.
lengths = [3, 2, 0, 2]


### Quinto ejercicio

# Estamos usando listas para llevar un conteo de las personas que vinieron a la fiesta, y en el orden en que llegaron.
# Por ejemplo, la siguiente lista representa una fiesta de 7 invitados, en donde adela llegó primera y
# ford fue el último en llegar:
# party_attendees = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford']

# Un invitado es considerado 'fashionably late' si llegan al menos después de la mitad de todos los invitados. 
# De todas formas, ellos no deberían ser los ultimos invitados. En el ejemplo de abajo,
# Mona y Gilbert son los únicos invitados "fashionably late".

# Completa la función de abajo que toma una lista de invitados 
# asi como a cada persona, y nos dice cuando una persona es fashionably late.
def fashionably_late(arrivals, name):
    """Given an ordered list of arrivals to the party and a name, return whether the guest with that
    name was fashionably late.
    """
    arrivals_length = len(arrivals)

    half_arrivals = (arrivals_length // 2)
    
    if half_arrivals % 2 != 0:
        half_arrivals = half_arrivals + 1

    if name == arrivals[-1]:
        return False
    elif name in arrivals[half_arrivals:]:
        return True
    else:
        return False