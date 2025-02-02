const name = "hitesh"

const repoCount = 50

// console.log(name + " " + repoCount + " value")

// console.log(`Hello my name is ${name} and my repo count is ${repoCount}`); // String Interpolration


const game = new String('Jatin-35')

console.log(game[0])
console.log(game.__proto__)

console.log(game.length);

console.log(game.toUpperCase());
console.log(game.charAt(2));

console.log(game.indexOf('t'));

const newString = game.substring(0,2)
console.log(newString);

const anotherString = game.slice(-9, 5)
console.log(anotherString)

const newStringOne = "    Jatin123    "
console.log(newStringOne);
console.log(newStringOne.trim());

const url = "https://hitesh.com/hitesh%20choudhary"

console.log(url.replace('%20','-'))

console.log(url.includes('hitesh'))
console.log(url.includes('hootesh'))

console.log(game.split('-'));
