#Solution for Level 3 Challenge

***Expected parameters:*** input_string

***Sample Input:***
input_string = "noonabbada"

***Sample Output:***
3 // noon | abba | d | a

***Time Complexity:***
O(n^2) for the possible substrings (remaining_letters) and checking the best palindrome cuts
O(n) for sorting the palindromes

=O(n^2 x n)
=O(n^3)

***Space Complexity***
O(n^2) for the recursion on remaining_letters
O(n) for the palindrome cuts (stored in 1 dimensional array)

=O(n^2 x n)
=O(n^3)


```javascript
function getPalindromeCuts(input_string) {
    //first, declare the variables that we want to compute using this function
    var palindromes = []; //will contain all the best palindrome cuts within the  input string
    var remaining_letters = []; // will contain all the letters that are not palindrome and those not yet checked if palindrome
    var sorted_palindromes = []; //will contain the sorted palindrome cuts based on the input string


    //first, remove the spaces in the input string
    input_string = input_string.replaceAll(' ', '');

    //copy the value of input string to the remaining letters
    //initially, all letters are not yet checked
    remaining_letters = input_string;
    /*  remaining_letters = "noonabbada" */

    //loop thru the input string and check the best palindrome cuts, from the beginning to end of the string
    for (i = 0; i < input_string.length; i++) {
        //recursive checking of the possible best cuts in the remaining letters
        //use the function created in the Level 2 Challenge
        var palindrome = getLongestPalindrome(remaining_letters);

        //check if there is a palindrome within the remaining_letters
        if (palindrome) {
            //if the has a palindrome, add it in the array of palindromes
            palindromes.push(palindrome);

            //remove that palindrome cut from the remaining letters
            remaining_letters = remaining_letters.replaceAll(palindrome, '');
        }

        /*
            palindrome = "noon"
            palindromes = ["noon"]
            remaining_letters = "abbada"

            =================================

            palindrome = "abba"
            palindromes = ["noon", "abba"]
            remaining_letters = "da"
        */
    }



    //sort the saved palindromes from the array based on its position in the input string
    $.each(palindromes, function(key, value) {
        var position_in_string = input_string.lastIndexOf(value);
        sorted_palindromes[position_in_string] = value;

        /*
            value ="noon"
            position_in_string = 0
            sorted_palindromes = [0=>"noon"]

            =================================

            value ="abba"
            position_in_string = 4
            sorted_palindromes = [0=>"noon", 4=>"abba"]
        */

    });

    //include the remaining letters from the input string that are not palindromes
    if (remaining_letters.length > 0) {
        //sort the remaining_letters from the array based on its position in the input string
        $.each(remaining_letters.split(''), function(key, value) {
            var position_in_string = input_string.lastIndexOf(value);
            sorted_palindromes[position_in_string] = value;

            /*
            value ="d"
            position_in_string = 8
            sorted_palindromes = [0=>"noon", 4=>"abba", 8=>"d"]

            ====================================================

            value ="a"
            position_in_string = 9
            sorted_palindromes = [0=>"noon", 4=>"abba", 8=>"d", 9=>"a"]
            */
        })
    }

    //make sure that the elements of the sorted_palindrome is not empty
    sorted_palindromes = sorted_palindromes.filter(Boolean);

    //return the value of the currently considered 'best palindrome cuts' inside the string
    //return how many cuts are there and display the sorted palindromes array
    return (sorted_palindromes.length - 1) + ' <code>//' + sorted_palindromes.join(' | ') + '</code>';
}



```