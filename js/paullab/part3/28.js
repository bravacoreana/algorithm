function twogram(string) {
  const arr = string.split("");
  for (let i = 0; i < arr.length - 1; i++) {
    console.log(`${arr[i]} ${arr[i + 1]}`);
  }
}

twogram("hello");
