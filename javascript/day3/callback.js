// function A(callback){
//     callback();
// }

// function B(){
//     console.log("나는 B 함수야.");
// }

// function findUser(id, cb){
//     const user = {
//         id: id,
//         name: "User" + id,
//         email: id + "@test.com",
//     };
//     cb(user);
// }

// findUser(1, function (user){
//     console.log("user: ", user);
// });

function findUser(id, cb){
    setTimeout(function(){
        const user = {
            id: id,
            name: "User" + id,
            email: id + "@test.com",
        };
        cb(user);
    }, 1000);
}

findUser(1, function (user){
    console.log("user: ", user);
});
console.log("finish!");