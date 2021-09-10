// << 9. concat을 활용한 출력 방법 >>

/* 다음 소스 코드를 완성해 날짜와 시간을 출력해라.

var year = "2019";
var month = "04";
var day = "26";
var hour = "11";
var minute = "34";
var second = "27";

var result = // START FROM HERE //
console.log(result); // 2019/04/26 11:34:27

*/

var year = "2019";
var month = "04";
var day = "26";
var hour = "11";
var minute = "34";
var second = "27";

var result = `${year}/${month}/${day} ${hour}:${minute}:${second}`;
console.log(result);
