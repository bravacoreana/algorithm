// << 문제 1. 배열의 삭제 >>
// 다음 배열에서 400, 500을 삭제하는 코드를 입력하세요.

var nums = [100, 200, 300, 400, 500];

// - 1
nums = nums.splice(0, 3);

// - 2
nums.pop();
nums.pop();

// - log
console.log(nums);
