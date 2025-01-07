var amounts: any = 0
console.log(typeof amounts)

if(amounts === 0){
    console.log('Hola');
}

amounts = "Hola "

console.log(amounts.repeat(3));

console.log(typeof amounts)

const tries = (num: Number) => {
    const rounded_number = Math.round(+num)
    const rounded_number2 = Math.round(+num * 1.3)

    console.log({number1: rounded_number, number2: rounded_number2});
    
    return [rounded_number, rounded_number2]
}

console.log(tries(1.444));
