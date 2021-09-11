const scores = prompt("type the score").trim().split(" ");

let total = 0;
scores.forEach((score) => {
  let scoreToInt = parseInt(score, 10);
  total += scoreToInt;
});

const avgScore = total / scores.length;

console.log(avgScore);
