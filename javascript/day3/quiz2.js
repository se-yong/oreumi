// 주어진 숫자에서 10을 만들기 위해 얼마를 더해야 하는지 계산한 후, 프로미스를 사용하여 결과를 반환하는 함수 makeTenWithPromise를 작성하세요.
// 1. makeTenWithPromise 함수는 숫자를 매개변수로 받습니다.
// 2. makeTenWithPromise 함수는 프로미스 객체를 반환해야 합니다.
// 3. 프로미스는 숫자에서 10을 만들기 위해 필요한 값을 성공적으로 전달해야 합니다.
// 4. 숫자가 유효하지 않은 경우, 프로미스는 에러를 반환해야 합니다. 에러 메시지는 "유효하지 않은 숫자입니다."입니다.

function makeTenWithPromise(number) {
    return new Promise((resolve, reject) => {
        if (typeof number !== 'number') {
            reject(new Error('유효하지 않은 숫자입니다.'));
        }
        else {
            const amountToAdd = 10 - number;
            resolve(amountToAdd);
        }
    });
}

makeTenWithPromise('5')
    .then((amount) => {
        console.log('더해야하는 값:', amount);
    })
    .catch((error) => {
        console.log('에러:', error);
    })
