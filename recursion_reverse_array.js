reverse_recursion = (array) => {
    n = array.length
    
    if (n <= 1) return array

    return reverse_recursion(array.slice(1)).concat(array[0])
}

reverse_forloop = (array) => {
    to_return = []

    for (let i = 0; i < array.length; i++) {
        to_return.unshift(array[i])
    }

    return to_return
}

time1 = Date.now()

for (let i = 0; i < 998; i++) {
    reverse_recursion(Array(i).fill(0))
}

time2 = Date.now()

for (let i = 0; i < 998; i++) {
    reverse_forloop(Array(i).fill(0))
}

time3 = Date.now()

console.log(`Recursif: ${time2-time1} ms`)
console.log(`For-loop: ${time3-time2} ms`)


console.log( reverse_recursion([0,1,2,3,4,5]) )
console.log( reverse_forloop([0,1,2,3,4,5]) )
