function voting(lists) {
  result = {};
  const arr = lists.split(" ");
  arr.forEach((el) => {
    // result[el] += 1;
    Object.keys(result).includes(result[el])
      ? (result[el] += 1)
      : (result[el] = 0);
  });
  return result;
}

console.log(voting("liha bilbo bilbo"));
