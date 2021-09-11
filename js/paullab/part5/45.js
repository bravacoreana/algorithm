const currentDate = new Date();

let year = currentDate.getTime();
year = Math.floor(year / (1000 * 3600 * 24 * 365)) + 1970;
console.log(year);
