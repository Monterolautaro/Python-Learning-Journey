// Hagamos el siguiente ejercicio: El usuario debe poder
// ingresar por algún método una serie de números separados por comas,
//  como por ejemplo "3,7,5,9,1", el programa debe poder separar cada
//   uno de los números y ordenarlos del mas pequeño al mas grande.

// Puedes usar el lenguaje que desees, consultar en Internet o a cualquier IA sin problema,
//  lo que estamos evaluando es la manera en que resuelve el problema, no el lenguaje o experiencia para resolverlo.


const organizeNumbers = (numString) => {
    let numbers = numString.split(', ').map((number) => +number).sort();
    return numbers
}

console.log(organizeNumbers('3, 4, 1, 7, 9'));