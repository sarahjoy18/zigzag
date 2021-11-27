# Solution for Level 1 Challenge

***Expected parameters:*** 

input_string


***Sample Input:***

input_string = "Nurses run"


***Sample Output:***

true


***Time Complexity:***

O(1) - Constant time, no matter how big the input string is, it takes the same amount of time to get the palindrome


***Space Complexity:***

O(1) - Constant space


```javascript

function isPalindrome(input_string) {
    //remove the spaces in the input string first
    input_string = input_string.replaceAll(' ', '');
    // >Nursesrun

    //change all letters to lowercase
    input_string = input_string.toLowerCase();
    // >nursesrun

    //separate the input string per letter and put it into an array
    var letters = input_string.split('');
    // >letters = ['n','u','r','s','e','s']

    //reverse the elements inside the array and store it in an array variable
    var reversed_array = letters.reverse();
    // >reversed_array = ['n','u','r','s','e','s']

    //join the array elements (reversed) into a new string
    var reversed_string = reversed_array.join('');
    // >reversed_string = nursesrun

    //compare the reversed string with the input string 
    //if it has the same value, then it is considered a palindrome
    //return the result of comparison
    return input_string === reversed_string;
    // >true

    //The code above could also be optimized into a one line of code 
    //like this
    // return input_string == input_string.replaceAll(' ', '').toLowerCase().split('').reverse().join('');
}


```