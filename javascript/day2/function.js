// 1. 함수를 선언
function add(a, b) {
    return a + b;
}

let addNumbers = add(3, 5);
console.log(addNumbers);

// 2. 함수 표현식
const substract = function(a, b){
    return a - b;
}

console.log(substract(5, 3));

// 3. 화살표 함수
let substract2 = (a, b) => {
    return a - b;
}
console.log(substract2(7, 5));