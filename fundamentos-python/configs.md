# **Primer paso**

*El primer paso para trabajar con Python es crear un entorno virtual*
```bash
 - Se utiliza este comando: " python -m venv <Nombre_del_venv> " 
```
Nota: Por convención, el nombre más común es venv

```bash
 - Se debe activar el entorno virtual: " source <Nombre_del_venv>/bin/activate "
```

# **Segundo paso**

 *Luego de haber activado el venv y haber instalado las dependencias necesarias del proyecto, generamos el archivo requirement.txt*

```bash
 - Para instalar dependencias se usa: " pip install <nombre_del_paquete> "
```

```bash
 - Utilizamos el comando " pip freeze > requirements.txt "
```

**En este punto ya podremos empezar a trabajar en nuestro proyecto**

*Cuando terminamos de trabajar en el proyecto, desactivamos el entorno virtual*

```bash
- Para ello, se utiliza este comando: " deactivate "
```

**Recordatorio**

*Siempre generar el archivo .gitignore y añadir el entorno virtual ahí*

-
-
-
-
-
## **Tipos de modelos de IA**

-  ### _Modelo de Regresión_
```bash
Este modelo tiene como capa de salida, un número, como en el de conversión de celsius a fahrenheit, o
también en donde se calcule un valor para una casa, teniendo en cuenta datos como m2, número de baños,
número de cuartos, si tiene pileta o no, etc. Siempre la capa de salida en un modelo de regresión, va 
a ser un número.
```

- ### _Modelo de Clasificación_
```bash
Este modelo tiene como capa de salida, un string clasificatorio. Por ejemplo, un sistema en donde se
pase como entrada una imagen, y el modelo me devuelva a qué clasificación pertenece (ropa, inmuebles, etc).
Más especifico aún, sería un modelo para una tienda de ropa, el cual se encargue de clasificar las prendas
que se pasan como imagen (pantalón, remera, buzo, sweater, etc).
```

