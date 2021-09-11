function isPrimeNumber(number) {
  if (number <= 1) {
    console.log("no");
    return;
  }
  if (number % 2 === 0) {
    console.log("no");
    return;
  }
  for (i = 3; i < number; i += 2) {
    if (number % i !== 0) {
      console.log("yes");
      return;
    }
    console.log("no");
    return;
  }
}

isPrimeNumber(20);

function isPrimeNumber2(number) {
  if (
    isNaN(number) |
    (number <= 1) |
    (number % 2 === 0) |
    (number % 3 === 0) |
    (number % 5 === 0) |
    (number % 7 === 0)
  ) {
    console.log("no");
  } else {
    console.log("yes");
  }
}

isPrimeNumber2(19);
