const numbers = prompt("numbers").trim().split(" ");

function sorting(numbers) {
  numbers.sort((a, b) => b - a);
  numbers.forEach((number) => parseInt(number, 10));
  return numbers;
}

console.log(...sorting(numbers));
