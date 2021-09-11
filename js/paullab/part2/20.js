const numbers = prompt("give us two numbers").trim().split(" ");
const a = parseInt(numbers[0] / numbers[1]);
const b = numbers[0] % numbers[1];

console.log(a, b);
