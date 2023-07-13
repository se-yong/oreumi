let numbers = [1, 2, 3, 4, 5];

numbers.push(6);
numbers.pop();
numbers.splice(1, 2); // 인덱스 삭제
console.log(numbers);
let numbers1 = numbers.slice(1, 2); // 슬라이싱
console.log(numbers1);
console.log(numbers.length);
console.log(numbers[2]);