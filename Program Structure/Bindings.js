// Bindings help to catch and store variables into local state

let caught = 6 * 6
console.log(caught)

// After a binding has been declared it can be used as an expression

let cell = 10
console.log( cell * cell)

// bindings do not contain values they grab them 
// Two bindings can refer to the same value

let studentLoans = 33000
studentLoans = studentLoans - 2000;
console.log(studentLoans)

// Anything that produces a value is a considered a JavaScript Expression

console.log(Math.max(100, 231))

console.log(Math.min(312, 310) + 123)