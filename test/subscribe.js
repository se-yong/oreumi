// script.js
let isSubscribed = false; // 초기 상태: 구독하지 않은 상태

function toggleSubscription() {
    let subscribeButton = document.getElementById('subscribeButton');
    
    if (isSubscribed) {
        // 이미 구독 중이면 구독 취소 처리
        unsubscribe();
        subscribeButton.innerHTML = '구독';
        subscribeButton.classList.remove('disabled');
    } else {
        // 아직 구독하지 않은 상태면 구독 처리
        subscribe();
        subscribeButton.innerHTML = '구독 중';
        subscribeButton.classList.add('disabled');
    }
    
    // 상태 반전
    isSubscribed = !isSubscribed;
}

function subscribe() {
    // 여기에 구독 처리에 필요한 로직 작성
    console.log('구독 완료');
}

function unsubscribe() {
    // 여기에 구독 취소 처리에 필요한 로직 작성
    console.log('구독 취소 완료');
}
