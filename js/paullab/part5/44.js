function sum(number) {
  let total = 0;
  let arr = number.toString().split("");
  arr.map((el) => {
    total += parseInt(el, 10);
  });
  return total;
}

console.log(sum(5231));

/*

let n = prompt('숫자를 입력하세요.');
let sum = 0;

while(n !== 0){
  sum += (n % 10);
  n = Math.floor(n/10);
}

console.log(sum);

*/
