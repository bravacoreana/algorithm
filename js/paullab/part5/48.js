function fixIt(str) {
  let newWord = [];
  str.split("").map((el) => {
    if (el.toUpperCase() === el) {
      newWord.push(el.toLowerCase());
    } else {
      newWord.push(el.toUpperCase());
    }
    return newWord;
  });
  return newWord.join("");
}

console.log(fixIt("helLO"));
