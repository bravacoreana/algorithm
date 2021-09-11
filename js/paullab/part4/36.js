function gugu(number) {
  let result = "";
  for (let i = 1; i <= 9; i++) {
    result += i * number + " ";
  }
  console.log(result);
}

gugu(3);
