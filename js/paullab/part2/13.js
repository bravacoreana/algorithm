const arr = ['수성', '금성','지구','화성','목성','토성','천왕성','해왕성']

function star(number) {
    number > arr.length || number <= 0 
    ? console.log("are you insane") 
    : console.log(arr[number-1])
}
star(0)