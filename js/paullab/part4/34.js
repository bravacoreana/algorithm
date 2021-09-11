const heights = prompt("heights").trim();

function checkHeights(heights) {
  let newArr = heights.split(" ");
  newArr.sort((a, b) => a - b);
  newArr.join(" ") === heights ? console.log("YES") : console.log("NO");
}

checkHeights(heights);
