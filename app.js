//random
function shuffle(array) {
    let currentIndex = array.length,
        randomIndex;

    // While there remain elements to shuffle...
    while (currentIndex != 0) {

        // Pick a remaining element...
        randomIndex = Math.floor(Math.random() * currentIndex);
        currentIndex--;

        // And swap it with the current element.
        [array[currentIndex], array[randomIndex]] = [
            array[randomIndex], array[currentIndex]
        ];
    }

    return array;
}

// Used like so
var arr = [2, 11, 37, 42];
shuffle(arr);
console.log(arr);

//buildings

function buildings(arr) {
    var newArr = []
    for(var i = 1;i<arr.length;i++){
        if(arr[i] > 0 && arr[i] > arr[i-1] ){
            newArr.push(arr[i])
        }
        console.log(newArr) 
    }
}
buildings([0,4]);

//zip it

function zipIt(arr1,arr2){
    var arr3 = []
    for(var i=0;i<arr1.length;i++){
        arr3.push(arr1[i]);
    }
    for(var j = 0;j<arr2.length;j++){
        arr3.push(arr2[j])
    }

        console.log(arr3)
    }

zipIt([5,7,9,11],[20,30,40,50])

console.log(1 + 2 + "3" + "4" + 5 + 6);


// 1. Get 1 to 255 - Write a function that returns an array with all the numbers from 1 to 255

// function allNums () {
//     var arr = []
//     for(var i = 1;i<256; i++){
//         arr.push(i);
//     }
//     console.log(arr)
//     return arr
// }

// allNums()

// 2. Get even 1000 - Write a function that would get the sum of all the even numbers from 1 to 1000.
//   You may use a modulus operator for this exercise

// function getEven() {
//     var sum = 0
//     for(var i = 0;i<1001; i++){
//         if (i % 2 === 0){
//             sum += i
//         }
//     }
//     console.log(sum)
// }
// getEven();

// 3. Sum odd 5000 - Write a function that returns the sum of all the odd numbers
//  from 1 to 5000. (e.g. 1+3+5+...+4997+4999)

// function sumOdd() {
//     var sum = 0;
//     for(var i = 0; i < 5001; i++){
//         if(i % 2 === 1){
//             sum += i
//         }
//     }
//     console.log(sum);
// }
// sumOdd();

// 4. Iterate an array - Write a function that returns the sum of all the values within an array.
//  (e.g. [1,2,5] returns 8. [-5,2,5,12] returns 14)

// function all_vals(arr){
//     var sum = 0;
//     for(i = 0;i< arr.length;i++){
//         sum += arr[i]
//     }
//     console.log(sum);
// }

// all_vals([1,2,3,4,5]);

// 5. Find max - Given an array with multiple values, write a function that returns the maximum number in the array. (e.g. for [-3,3,5,7] max is 7)

// function find_max(arr){
//     var max = 0;
//     for(i=0;i<arr.length;i++){
//         if(arr[i] > max){
//             max = arr[i]
//         }
//     }
//     console.log(max)
// }

// find_max([1,2,3,4,5]);

// 6. Find average - Given an array with multiple values, write a function that returns the average of the values in the array. (e.g. for [1,3,5,7,20] average is 7.2)

// function find_avg(arr){
//     var sum = 0;
//     for(i = 0;i<arr.length;i++){
//         sum += arr[i]
//     }
//     var avg = (sum/arr.length)
//     console.log(avg)
// }

// find_avg([1,2,3,4,5,6,7]);

// 7. Array odd - Write a function that would return an array of all the odd numbers between 1 to 50. 
// (ex. [1,3,5, .... , 47,49]). Hint: Use 'push' method

// function odd(){
//     var odd_arr = [];
//     for(i = 0;i<51;i++){
//         if (i % 2 === 1){
//             odd_arr.push(i)
//         }
//     }
//     console.log(odd_arr)
// }

// odd();

// 8. Greater than Y - Given value of Y, write a function that takes an array and 
// returns the number of values that are greater than Y. For example if arr = [1, 3, 5, 7] and 
// Y = 3, your function will return 2. (There are two values in the array greater than 3, which are 5, 7)

// var arr = [1,2,3,4,5,6,7,8,9,34,56,67,78,89]
// function greater_than_y(y){
//     var num = 0;
//     for(i = 0;i<arr.length;i++){
//         if(arr[i] > y){
//             num += 1
//         }
//     }
//     console.log(num)
// }
// greater_than_y(10);

// 9. Squares - Given an array with multiple values, write a function that replaces each value in the array 
// with the value squared by itself. (e.g. [1,5,10,-2] will become [1,25,100,4])

// function squares(arr){
//     for(i = 0;i<arr.length;i++){
//         arr[i] = (arr[i]*arr[i])
//     }
//     console.log(arr)
// }

// squares([2,3,4,5,6]);

// 10. Negatives - Given an array with multiple values, write a function
//  that replaces any negative numbers within the array with the value of 0. 
//  When the program is done the array should contain no negative values. (e.g. [1,5,10,-2] will become [1,5,10,0])

// function no_negs(arr){
//     for(i = 0;i<arr.length;i++){
//         if(arr[i] < 0){
//             arr[i] = 0;
//         }
//     }
//     console.log(arr)
// }
// no_negs([-1, 3, 4, -5]);

// 11. Max/Min/Avg - Given an array with multiple values, write a function
//  that returns a new array that only contains the maximum, minimum, 
//  and average values of the original array. (e.g. [1,5,10,-2] will return [10,-2,3.5])

// function maxMinAvg(arr){
//     var new_arr = [];
//     var sum = 0;
//     for(i=0;i<arr.length;i++){
//         sum += arr[i];
//     }
//     new_arr.push(Math.max(...arr))
//     new_arr.push(Math.min(...arr))
//     new_arr.push(sum/arr.length)
//     console.log(new_arr)
// }

// maxMinAvg([3,5,7,9,4,6,8]);

// var arr = [42,68,7,21,243,512];
// for(var x = arr.length-2;x>1;x--){
//     arr[x-1] = arr[x+1];
// }

// console.log(x);

// 