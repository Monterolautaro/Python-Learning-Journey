# Teoría sobre librerías externas en python

En esta sección estará la teoría vinculada al archivo de práctica: [libraries](./libraries.py)

# Indice

1. [imports](#imports)
2. [Three tools for understanding strange objects](#three-tools-for-understanding-strange-objects)

## Imports
Algunas de las librerias están en la "standard library", significando que se pueden encontrar en cualquier lugar que se corra Python. Otras librerias, pueden ser fácilmente añadidas, inclúso si no siempre están en la "standard library" de Python.

- ***De cualquier forma, podemos acceder a este código a través de*** _imports_
    - ***vamos a empezar el ejemplo importando*** _maths_ ***de la "standard library"***
```bash
import math

print("It's math! It has type {}".format(type(math)))

# Salida: It's math! It has type <class 'module'>
```
- math ***es un modulo. Un modulo es simplemente una colección de varibales definidas por alguien más. Podemos ver todos los nombres en math usando la función dir().***
```bash
print(dir(math))

# Salida: ['__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']
```
- ***Podemos acceder a estas variabes usando la sintaxis por punto. Algunas de ellas son simples valores, como*** _math.pi:_
```bash
print("pi to 4 significant digits = {:.4}".format(math.pi))

# Salida: pi to 4 significant digits = 3.142
```
- ***Pero la mayoría de lo que vamos a encontrar en el módulo son funciones, como*** _math.log:_
```bash
math.log(32, 2)

# Salida: 5.0
```

###  Otra sintaxis de importación
Si sabemos que vamos a estar usando funciones en math frequentemente podemos importarlas con un alias corto para ahorrar escribir (Aunque en este caso "math" ya es bastante corto)
```bash
import math as mt
mt.pi

# Salida: 3.141592653589793
```
***¿No sería buenisimo si pudieramos referirnos a todas las variables en el modulo de math por ellas mismas? i.e. ¿Si pudieramos solo referirnos a*** pi ***en lugar de*** math.pi ***o*** mt.pi? ***Buenas noticias: si podemos.***
```bash
from math import *
print(pi, log(32, 2))

# Salida: 3.141592653589793 5.0
```

- _imports *_ ***hace que todas las variables de un módulo sean accesibles sin necesidad de usar la sintaxis por punto. Pero esto puede conllevar errores, si hay librerias con funciones que tengan el mismo nombre pero reciban distintos argumentos, o cumplan roles distintos. Por ejemplo:***
```bash
from math import *
from numpy import *
print(pi, log(32, 2))

# Salida: TypeError                                 Traceback (most recent call last)
# /tmp/ipykernel_19/3018510453.py in <module>
#       1 from math import *
#       2 from numpy import *
# ----> 3 print(pi, log(32, 2))

# TypeError: return arrays must be of ArrayType
```
- ***Un buen compromiso es importar solo las cosas especificas que vamos a necesitar de cada modulo.***
```bash
from math import log, pi
from numpy import asarray
```

### Submodulos
Hemos visto que los modulos contienen variables que pueden referirse a funciones o valores. A veces, podemos encontrar variables refiriendose a otros modulos.
```bash
import numpy
print("numpy.random is a", type(numpy.random))
print("it contains names such as...",
      dir(numpy.random)[-15:]
     )

# Salida: numpy.random is a <class 'module'>
# it contains names such as... ['seed', 'set_state', 'shuffle', 'standard_cauchy', 'standard_exponential', 'standard_gamma', 'standard_normal', 'standard_t', 'test', 'triangular', 'uniform', 'vonmises', 'wald', 'weibull', 'zipf']
```
- ***Asi que si importamos numpy, despues llamar a una funcion en el "submodulo"*** random, ***va a requerir dos puntos.***
```bash 
# Roll 10 dice
rolls = numpy.random.randint(low=1, high=6, size=10)
rolls

# Salida: array([3, 4, 3, 4, 5, 5, 2, 1, 3, 3])
```
**Oh the places you'll go, oh the objects you'll see¶**
A medida que vayamos trabajando con distintas librerias para tareas especializadas, vamos a encontrar que cada una define su propios types que vamos a tener que aprender para trabajar con cada libreria. Por ejemplo, si trabajamos graficando con matplotlib, vamos a estar en contacto con los objetos que define los cuales representan Subplots, figuras, TickMarks, y Annotations. En las funciones de pandas, nos vamos a encontrar con DataFrames y Series.

En esta sección estaremos abordando una guía de supervivencia para trabajar conlos types de las librerias externas de Python.

## Three tools for understanding strange objects
En la anterior celda, vimos que llamar a la funcion de numpy nos trae un "array".. No hemos visto algo como eso antes (No en esta documentación). Por eso, tenemos tres herramientas que nos ayudan a entender estos objetos.

1. _type()_ (¿Qué es esto?)
```bash
type(rolls)

# Salida: numpy.ndarray
```

2. _dir()_ (¿Que puedo hacer con esto?)
```bash
print(dir(rolls))

# Salida: ['T', '__abs__', '__add__', '__and__', '__array__', '__array_finalize__', '__array_function__', '__array_interface__', '__array_prepare__', '__array_priority__', '__array_struct__', '__array_ufunc__', '__array_wrap__', '__bool__', '__class__', '__complex__', '__contains__', '__copy__', '__deepcopy__', '__delattr__', '__delitem__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__iand__', '__ifloordiv__', '__ilshift__', '__imatmul__', '__imod__', '__imul__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__ior__', '__ipow__', '__irshift__', '__isub__', '__iter__', '__itruediv__', '__ixor__', '__le__', '__len__', '__lshift__', '__lt__', '__matmul__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmatmul__', '__rmod__', '__rmul__', '__ror__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__setitem__', '__setstate__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__xor__', 'all', 'any', 'argmax', 'argmin', 'argpartition', 'argsort', 'astype', 'base', 'byteswap', 'choose', 'clip', 'compress', 'conj', 'conjugate', 'copy', 'ctypes', 'cumprod', 'cumsum', 'data', 'diagonal', 'dot', 'dtype', 'dump', 'dumps', 'fill', 'flags', 'flat', 'flatten', 'getfield', 'imag', 'item', 'itemset', 'itemsize', 'max', 'mean', 'min', 'nbytes', 'ndim', 'newbyteorder', 'nonzero', 'partition', 'prod', 'ptp', 'put', 'ravel', 'real', 'repeat', 'reshape', 'resize', 'round', 'searchsorted', 'setfield', 'setflags', 'shape', 'size', 'sort', 'squeeze', 'std', 'strides', 'sum', 'swapaxes', 'take', 'tobytes', 'tofile', 'tolist', 'tostring', 'trace', 'transpose', 'var', 'view']
```

3. _help()_ (Dime mas)
```bash
help(rolls.ravel)
# Salida: Help on built-in function ravel:

# ravel(...) method of numpy.ndarray instance
#     a.ravel([order])
    
#     Return a flattened array.
    
#     Refer to `numpy.ravel` for full documentation.
    
#     See Also
#     --------
#     numpy.ravel : equivalent function
    
#     ndarray.flat : a flat iterator on the array.
```

Para saber mas acerca de los numpy arrays, puedes ver la documentación oficial [Aquí](https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.ndarray.html)


### Operator overloading
¿Cuál es el valor de la siguiente expresión?
```bash
[3, 4, 1, 2, 2, 1] + 10

# Salida: TypeError                                 Traceback (most recent call last)
# /tmp/ipykernel_19/2144087748.py in <module>
# ----> 1 [3, 4, 1, 2, 2, 1] + 10

# TypeError: can only concatenate list (not "int") to list
```
Que pregunta mas obvia. Of course, es un error.

Pero que hay de...
```bash 
rolls + 10

# Salida: array([13, 14, 13, 14, 15, 15, 12, 11, 13, 13])
```
Podríamos pensar que Python regula estrictamente cómo se comportan las piezas de su sintaxis central, como +, <, in, == o los corchetes para indexación y slicing. Pero, en realidad, adopta un enfoque muy flexible. Cuando defines un nuevo tipo, puedes decidir cómo funciona la suma para él, o qué significa que un objeto de ese tipo sea igual a otra cosa.

Los diseñadores de las listas decidieron que añadirlos a los números no estaba permitido. Los diseñadores de los arrays de numpy hacen una cosa diferente (añadir el número a cada elemento del array).

Aca hay un par de ejemplos de como los arrays de numpy interactuan inesperadamente con los operadores de Python (O por lo menos diferentemente de las listas).

```bash
# At which indices are the dice less than or equal to 3?
rolls <= 3

# Salida: array([ True, False,  True, False, False, False,  True,  True,  True, True])
```
```bash
xlist = [[1,2,3],[2,4,6],]
# Crear un array 2D
x = numpy.asarray(xlist)
print("xlist = {}\nx =\n{}".format(xlist, x))

# Salida: xlist = [[1, 2, 3], [2, 4, 6]]
        #  x =
        # [[1 2 3]
        # [2 4 6]]
```
```bash
# Toma el ultimo elemento de la segunda fila del array de numpy
x[1,-1]

# Salida: 6
```
```bash
# Toma el ultimo elemento de la segunda sublista de nuestra lista anidada?
xlist[1,-1]

# Salida: TypeError                                 Traceback (most recent call last)
# /tmp/ipykernel_19/3020169379.py in <module>
    #   1 # Get the last element of the second sublist of our nested list?
# ----> 2 xlist[1,-1]

# TypeError: list indices must be integers or slices, not tuple
```

**When does 1 + 1 not equal 2?**

Deberías haber escuchado de (o iclúso usado) tensorflow, una libreria popularmente usada para deep learning. Hace un uso extensivo del operador overloading
```bash
import tensorflow as tf
# crea 2 constantes, cada una con un valor de 1
a = tf.constant(1)
b = tf.constant(1)
# Sumalas para obtener...
a + b

# Salida: <tf.Tensor: shape=(), dtype=int32, numpy=2>
```

- _a + b_ ***no es 2, es (citando la documentación de tensorflow)...***
    - ***un activador simbolico para uno de los outputs de una operación. No guarda los valores de esa operación, en vez de eso proporciona un medio para computar esos valores en una sesión de TensorFlow*** _tf.session_

Es importante solo tener en cuenta el hecho de que este tipo de cosas es posible y que las librerias a veces van a usar el operator overloading en maneras no obvias o magicas.

Entendiendo como funcionan los operadores de Python aplicados a ints, strings, y listas no garantiza que seas capaz de inmediatamente entender que hacen cuando se aplican a un **Tensor** de tensroflow, o a un **ndarray** de numpy, o a un **DataFrame** de pandas.

Una vez que hayas tenido un poco de experiencia trabajando con DataFrames, por ejemplo, una expresión como la siguiente se vuelve bastante intuitiva:
```bash
# Obtener las columnas sobre población mayor a 1m en sudamerica
df[(df['population'] > 10**6) & (df['continent'] == 'South America')]
```
Pero, ¿Cómo funciona exactamente? El anterior ejemplo caracteriza algo como 5 diferentes operadores overloaded. ¿Qué hacen cada uno de esas operaciónes? Puede ayudar a saber la respuesta cuando las cosas empiezan a salir mal.

- ***Alguna vez has llamado a*** help() ***o*** dir() ***sobre un objeto y preguntado dónde estaban todos esos nombres con doble guión bajo?***
```bash
print(dir(list))

# Salida: ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
```
Esto se vuelve directamente relacionado con operator overloading.

Cuando los programadores de python quieren definir como se comportan los operadores sobre sus tipos, ellos hacen eso implementando metodos con nombres especiales comenzando y terminando con 2 guiones bajos como ```__lt__```, ```__setattr__```, o ```__contains__```. Generalmente, nombres que siguen este formato tienen un significado especial para Python.

Así que, por ejemplo, la expresión x en [1, 2, 3] está de hecho llamando al metodo de lista ```__contains__``` por detras de escena. Es equivalente a ```[1, 2, 3].__contains__(x)```.

Para saber mas acerca de esto, podemos fijarnos en la [Documentación oficial de python](https://docs.python.org/3.4/reference/datamodel.html#special-method-names) que describe muchos de estos metodos de "guíon bajo".







