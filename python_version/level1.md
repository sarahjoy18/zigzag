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


```python
#This function is called by the AJAX Request when the check_btn is clicked
#It gets the string from the textbox

@views.route("/isPalindrome/<input_string>", methods=["POST", "GET"])
def isPalindrome(input_string):

    # compare the reversed string with the input string
    # if it has the same value, then it is considered a palindrome
    # return the result of comparison as json (response to ajax request)
    result = (input_string == input_string[::-1])
    return json.dumps(result)

```