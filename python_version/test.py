from werkzeug.wrappers import response


try:
    from main import app
    import unittest

except Exception as e:
    print("Some Modules are missing ".format(e))


class FlaskTest(unittest.TestCase):

    # check for the response 200
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/")
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    # check the return value of isPalindrome function
    def test_isPalindrome_content(self):
        tester = app.test_client(self)
        response = tester.post("/isPalindrome/madam")
        self.assertEqual(b'true', response.data)

    # check the return value of isPalindrome function
    def test_isPalindrome_content2(self):
        tester = app.test_client(self)
        response = tester.post("/isPalindrome/robot")
        self.assertEqual(b'false', response.data)

    # check the return value of getLongestPalindrome function
    def test_getLongestPalindrome_content(self):
        tester = app.test_client(self)
        response = tester.post("/getLongestPalindrome/banana")
        self.assertEqual(b'"anana"', response.data)

    # check the return value of getPalindromeCuts function
    def test_getPalindromeCuts_content(self):
        tester = app.test_client(self)
        response = tester.post("/getPalindromeCuts/noonabbada")
        self.assertTrue(b'3' in response.data)


if __name__ == "__main__":
    unittest.main()
