// // Primitive 

// // 7 types : String , Number , Boolean , null , undefined , Symbol , BigInt


// const id = Symbol('123');
// const anotherId = Symbol('123')

// console.log(id === anotherId);


// // const bigNumber =345213521235514554134513545343563662364256742n

// console.log(typeof bigNumber)


// // Reference Type (Non Primitive)

// // Array , Objects , Functions

// const heros = ["shaktiman" , "naagraj" , "doga"];

// let myObj = {
//     name :"hitesh",
//     age : 25,

// }

// const myFunction = function(){
//     console.log("Hello , World");
// } 

// console.log(typeof bigNumber)

// console.log(typeof myFunction)




// +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


// Stack(Primitive) , Heap(Non - primitive)


let myYoutubeName = "hiteshchoudary.com"

let anotherName = myYoutubeName;
anotherName = "hiteshcodes"

console.log(myYoutubeName);
console.log(anotherName);


let userOne = {
    name : "hitesh",
    age : 25,
    email : "xyz@gmail.com"

}


let userTwo = userOne;

userTwo.email = "hitesh123@gmail.com"

console.log(userOne.email)
console.log(userTwo.email)

