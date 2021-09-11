function countWords(string) {
  return string.split(" ").length;
}

console.log(countWords("buongiorno"));
console.log(
  countWords(
    "Lorem Ipsum is simply dummy text of the printing and typesetting industry."
  )
);
