const names = prompt("names").trim().split(" ");
const scores = prompt("scores").trim().split(" ");

let students = {};
names.forEach((name) => {
  scores.forEach((score) => (students[name] = score));
});

console.log(students);

// 답안
/*
const keys = prompt('이름을 입력하세요').split(' ');
const values = prompt('점수를 입력하세요').split(' ');
const obj = {};

for (let i=0; i<keys.length; i++) {
  obj[keys[i]] = parseInt(values[i], 10);
}

console.log(obj);
*/
