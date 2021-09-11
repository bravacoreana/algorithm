function whatDay(month, date) {
  const days = ["sun", "mon", "tue", "wed", "thu", "fri", "sat"];
  const inputValue = new Date(`2020-${month}-${date}`);
  return days[inputValue.getDay()];
}

console.log(whatDay(1, 1));
