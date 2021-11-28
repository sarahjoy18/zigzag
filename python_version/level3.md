# Solution for Level 3 Challenge

***Expected parameters:*** 
input_string


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


```python
#This function is called by the AJAX Request when the cut_btn is clicked
#It gets the string from the textbox

@ views.route("/getPalindromeCuts/<input_string>", methods=["POST", "GET"])
def getPalindromeCuts(input_string):
    palindromes = []  # will contain all the palindrome cuts
    remaining_letters = []  # will contain all the remaining letters per checking

    # will contain the sorted palindrome cuts and the remaining letters
    sorted_palindromes = []

    # remove the spaces from the input string
    input_string = input_string.replace(' ', '')

    # copy all the letters from the input string - initial value
    remaining_letters.append(input_string)
    # remaining_letters[0] = "noonabbada" 

    # loop thru all the letters of the input string
    for i in range(len(input_string)):
        # recursive checking as long as there are remaining letters
        if(i < len(remaining_letters)):
            # get the possible best palindrome cut
            # use the function created in the Level 2 Challenge
            # remove the surrounding qoutes since it is return as json
            palindrome = getLongestPalindrome(
                remaining_letters[i]).replace('"', '')

            # check if there's a palindrome in the remaining letters
            if (len(palindrome) > 1):
                # remove the palindrome from the set of remaining letters
                # needed to save the remaining letters in list because strings in python are immutable
                new_remaining_letters = remaining_letters[i].replace(
                    palindrome, '')

                # store the remaining letters for the next checking
                remaining_letters.append(new_remaining_letters)

                # store the palindrome in palindromes array to be sorted later
                position_in_string = input_string.rfind(palindrome)
                palindromes.append([position_in_string, palindrome])


                """
                    i = 0
                    palindrome = "noon"
                    position_instring = 0
                    palindromes = [[0,"noon"]]
                    remaining_letters[1] = "abbada"

                    =================================

                    i = 1
                    palindrome = "abba"
                    position_instring = 4
                    palindromes = [[0,"noon"], [4,"abba"]]
                    remaining_letters[2] = "da"


                """
            else:
                # else stop the recursive checking
                # because there is no palindrome in the remaining letters

                """

                i = 2
                remaining_letters[2] = "da"

                palindrome = ''
                palindromes = [[0,"noon"], [4,"abba"]]

                """
                break

    # add the remaining letter based on their position in the input string
    for remaining_letter in remaining_letters[-1]:
        position_in_string = input_string.rfind(remaining_letter)
        palindromes.append([position_in_string, remaining_letter])

        """
        palindromes = [[0,"noon"], [4,"abba"], [8,"d"], [9,"a"]]
        """

    # sort the palindromes based on their position in the input string
    for palindrome in enumerate(sorted(palindromes, key=lambda palindromes: palindromes[0]), start=1):
        sorted_palindromes.append(palindrome[1][1])

        """
        sorted_palindromes = ["noon", "abba", "d", "a"]
        """
        

    # set the value of result
    # return the value of the currently considered 'best palindrome cuts' inside the string
    # return how many cuts are there and display the sorted palindromes array
    result = '<b>'+str(len(sorted_palindromes)-1)+'</b> // ' + \
        ' | '.join(sorted_palindromes)

    # return the result markup to ajax request
    return json.dumps(result)

```
