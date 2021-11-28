# Solution for Level 2 Challenge

***Expected parameters:*** 
input_string


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

```python
#This function is called by the AJAX Request when the long_btn is clicked
#It gets the string from the textbox
@views.route("/getLongestPalindrome/<input_string>", methods=["POST", "GET"])
def getLongestPalindrome(input_string):
    # first, declare the variables that we want to compute using this function

    # will contain the value of the longest palindrome
    longest_palindrome = ""

    # will contain the length of the longest palindrome
    best_length = 0

    # remove the spaces in the input string
    input_string = input_string.replace(' ', '')
    total_len = len(input_string)

    # loop thru the letters of the input string
    # set each letter of the input string as the center
    for center in range(total_len):
        # check if total_length is even or odd
        if total_len % 2 == 0:
            # if even
            # check it from pair of letters from the center then outward
            left_pointer = center
            right_pointer = center+1


            """
                            --distance = 0
                *           --center = 0
                b a n a n a
                ^           --left pointer = 0
                  ^         --right pointer = 1
                
            """

        else:
            # if odd
            # check it from the centermost letter then outward
            left_pointer = center+1
            right_pointer = center+1

            """
            
                            --distance = 1 
                    *       --center = 2
                m a d a m
                  ^         --left pointer = 1
                      ^     --right pointer = 3

            """

        # start checking outward increment the distance from the center by 1
        for distance in range(total_len):

            # check if the pointers are within the range of the input string
            # this will save time, in case the center pointer doesn't have a valid prefix or suffix
            # because the left pointer or right pointer might have exceeded the input string
            if left_pointer >= 0 or right_pointer < total_len:

                """

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

                

                ======================================

                Additional checking when the left and right pointers exceeded the bounds of input string
                set the left pointer to 0 or the first letter
                and
                set the left pointer to total_len or the last letter

                """
                if(left_pointer < 0):
                    current_substring = input_string[0:right_pointer+1]
                elif(right_pointer >= total_len):
                    current_substring = input_string[left_pointer:total_len]
                else:
                    current_substring = input_string[left_pointer:right_pointer+1]

                # check if the current substring is not a single character
                if(len(current_substring) > 1):
                    # check if the current substring is a palindrome, reuse the function created in Level 1 Challenge
                    # compare if it has greater length than the currently considered 'best length'
                    # another checking is if it has the same length but positioned in the input string before the longest palindrome
                    if (isPalindrome(current_substring) == "true") and ((len(current_substring) > best_length) or (len(current_substring) > best_length and (input_string.rfind(current_substring) < input_string.rfind(longest_palindrome)))):
                        longest_palindrome = current_substring
                        best_length = len(current_substring)

            # keep moving the pointers outward
            left_pointer -= 1
            right_pointer += 1

    # after going thru all the letters of the input string
    # return the value of the currently considered 'longest palindrome'
    return json.dumps(longest_palindrome)


```
