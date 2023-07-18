// 주어진 숫자를 제곱한 후, 콜백 함수를 통해 결과를 전달하는 함수 squareWithCallback을 작성하세요.
// 1. squareWithCallback 함수는 숫자를 매개변수로 받습니다.
// 2. squareWithCallback 함수는 제곱한 결과를 콜백 함수를 통해 전달해야 합니다.
// 3. 콜백 함수는 두 개의 매개변수를 받아야 합니다. 첫 번째 매개변수는 에러 객체이며, 두 번째 매개변수는 제곱한 결과 숫자입니다.
// 4. 에러가 없는 경우, 콜백 함수는 null을 첫 번째 매개변수로 받고, 제곱한 결과를 두 번째 매개변수로 받아 호출해야 합니다.
// 5. 에러가 발생한 경우, 콜백 함수는 에러 객체를 첫 번째 매개변수로 받고, 두 번째 매개변수는 undefined로 설정하여 호출해야 합니다.


function squareWithCallback(number, callback) {
    if (typeof number !== "number") {
        const error = new Error("유효하지 않은 변수입니다");
        callback(error, undefined);
    } else {
        const result = number * number;
        callback(null, result);
    }
}

function callbackFunction(error, result) {
    if (error) {
        console.log('에러:', error);
    } else {
        console.log('결과:', result);
    }

}

squareWithCallback(4, callbackFunction);
squareWithCallback('hi', callbackFunction);