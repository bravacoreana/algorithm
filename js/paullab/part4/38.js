const scores = prompt("scores")
  .split(" ")
  .map(function (n) {
    return parseInt(n, 10);
  });

scores.sort((a, b) => a - b);

let count = 0;
let arr = [];

while (arr.length < 3) {
  let n = scores.pop();
  if (!arr.includes(n)) {
    arr.push(n);
  }
  count += 1;
}

console.log(count);
