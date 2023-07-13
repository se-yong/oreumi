function example() {
    let x = 10;
    if (true) {  // 블록 스코프
        let x = 20;
        console.log(x);
    }
    console.log(x);
}

example();