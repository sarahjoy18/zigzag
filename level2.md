#Solution for Level 2 Challenge

***Expected parameters:*** input_string


***Sample Input:***
input_string = "Banana"

***Sample Output:***
anana


***Sample Input:***
input_string = "Madama"

***Sample Output:***
madam

***Time Complexity:***
O(n^2) Quadratic for determining and checking if the current_substring is a palindrome with the best length

***Space Complexity: ***
O(1) - Constant Space for the longest_palindrome

```javascript
function getLongestPalindrome(input_string) {
    //first, declare the variables that we want to compute using this function

    var longest_palindrome = ""; //will contain the value of the longest palindrome
    var best_length = 0; //will contain the length of the longest palindrome
    var left_pointer = 0;
    var right_pointer = 0;

    //remove the spaces in the input string
    input_string = input_string.replaceAll(' ', '');

    //store the total length of the input string with no spaces in a variable
    //we will use it later multiple times
    var total_length = input_string.length;


    //loop thru the letters of the input string
    //set each letter as the center pointer
    for (center = 0; center < total_length; center++) {

        //check if total_length is even or odd
        if (total_length % 2 == 0) {
            //if even
            //check it from pair of letters from the center then outward
            left_pointer = center;
            right_pointer = center + 1;

            /*
                            --distance = 0
                *           --center = 0
                b a n a n a
                ^           --left pointer = 0
                  ^         --right pointer = 1
                
            */
        } else {
            //if odd
            //check it from the centermost letter then outward
            left_pointer = center - 1;
            right_pointer = center + 1;

            /*
            
                            --distance = 1 
                    *       --center = 2
                m a d a m
                  ^         --left pointer = 1
                      ^     --right pointer = 3

            */
        }

        //start checking outward increment the distance from the center by 1
        for (distance = 1; distance < total_length; distance++) {

            /*
                loop of pointers for even-length string
                ----------------------------
                ----------------------------

                            --distance = 1
                *           --center = 0
                b a n a n a
               ^            --left pointer = -1
                    ^       --right pointer = 2

                ----------------------------
                ----------------------------
                            --distance = 2
                *           --center = 0
                b a n a n a
             ^              --left pointer = -2
                      ^     --right pointer = 3

                ----------------------------
                ----------------------------

                            --distance = 3
                *           --center = 0
                b a n a n a
            ^               --left pointer = -3
                        ^   --right pointer = 4

                once the center iterated to 1

                            --distance = 0
                  *         --center = 1
                b a n a n a
                ^           --left pointer = 0
                    ^       --right pointer = 2



                --------------------------------
                --------------------------------



                loop of pointers for odd-length string
                ----------------------------
                ----------------------------

                            --distance = 2
                    *       --center = 2
                m a d a m
                ^           --left pointer = 0
                       ^    --right pointer = 4

                ----------------------------
                ----------------------------
                            --distance = 3
                    *       --center = 2
                m a d a m
               ^            --left pointer = -1
                          ^ --right pointer = 5
            
            */

            //check if the pointers are within the range of the input string
            //this will save time, in case the center pointer doesn't have a valid prefix or suffix 
            //because the left pointer or right pointer might have exceeded the input string
            if (left_pointer >= 0 || right_pointer < total_length) {

                //set the value of the current substring
                var current_substring = input_string.substring(left_pointer, right_pointer + 1);

                //check if the current substring is a palindrome, reuse the function created in Level 1 Challenge
                //compare if it has greater length than the currently considered 'best length'
                if (isPalindrome(current_substring) && best_length < current_substring.length) {

                    //declare it as the best length and the longest palindrome
                    best_length = current_substring.length;
                    longest_palindrome = current_substring;
                }
            }

            //keep moving the pointers outward
            left_pointer--;
            right_pointer++;
        }
    }

    //after going thru all the letters of the input string
    //return the value of the currently considered 'longest palindrome'
    return longest_palindrome;
}


```