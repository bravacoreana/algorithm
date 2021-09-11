function qtoe(letter) {
  if (letter.includes("q")) {
    return letter.replaceAll("q", "e");
  }
}

console.log(qtoe("querty"));
console.log(qtoe("hqllo my namq is hyqwon"));
