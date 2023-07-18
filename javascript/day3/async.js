async function wakeUp(){
    console.log("아침에 일어나서 강의듣기!");
}

async function eatLunch(){
    return new Promise((resolve, reject) => {
        setTimeout(function(){
            const data = "점심시간에 점심먹기!";
            resolve(data);
    }, 3000);
});
}

async function endClass(){
    console.log("강의가 끝났다! 놀아야지!");
}

async function startDay(){
    await wakeUp();
    const data = await eatLunch();
    console.log(data);
    await endClass();
}

startDay();
