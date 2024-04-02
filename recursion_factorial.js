

factorial_recursive = (n) => {
    if (n === 0) return 1
    return n * factorial_recursive(n-1)
}

factorial_forloop = (n) => {
    result = 1
    for (let i = 0; i<n; i++) {
        result *= n - i
    }
    return result
}

time1 = Date.now()

for (let i = 0; i < 998; i++) {
    factorial_recursive(i)
}

time2 = Date.now()

for (let i = 0; i < 998; i++) {
    factorial_forloop(i)
}

time3 = Date.now()


console.log(`Recursif: ${time2-time1} ms`)
console.log(`For-loop: ${time3-time2} ms`)


// console.log( factorial_recursive(10) )
// console.log( factorial_forloop(10) )
