const limit = prompt("limit");
const n = prompt("count");

let count = 0;
let total = 0;

for (let i = 1; i <= n; i++) {
  total += parseInt(prompt("weight"), 10);
  if (total <= limit) {
    count = i;
  }
}

console.log(count);
