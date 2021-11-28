## Zigzag Coding Challenge

### "Fun with Palindrome"
> Python3 and Flask Version
> 
### Author: Sarah Joy Lambino

> Date Created: Nov 28, 2021

> Date Modifed: Nov 28, 2021


The following codes are for:

1.  Determining if a string is a palindrome
    ```python
    def isPalindrome(input_string):
    ```

2.  Determining the longest palindromic substring
    ```python
    def getLongestPalindrome(input_string):
    ```

3.  Slicing string into set of palindromes and determine the minimum cut
    ```python
    def getPalindromeCuts(input_string):
    ```


***Related pages:*** 

                - main.py, 
                - website/views.py (Contains the solutions)
                - website/templates/index.html (Contains the input form and jQuery functions that call the AJAX requests)

***The solutions to the coding challenge was written in `Python3` using Flask framework ***

***The explanation to the solutions can be viewed in `level1.md`,`level2.md`,`level3.md`***


***To Test***

> Locally
1. Kindly download and install Python3.

Run the following commands in the terminal to: 

2.  Install virtualenv

    `pip install virtualenv`
3. Activate virtual env by running the following commands

    `python3 -m venv venv`
4. Install Flask
   
    `pip install flask`

5. Set Environment Variable for FLASK_APP

    `export FLASK_APP=main.py`

6. Run the Flask

    `flask run`


> Published
1. Go to [https://zigzag-py.herokuapp.com/](https://zigzag-py.herokuapp.com/)