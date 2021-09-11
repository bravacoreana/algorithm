function findWord(data, word) {
  if (data.includes(word)) {
    return data.indexOf(word);
  }
}

console.log(findWord("pineapple is yummy", "apple"));
