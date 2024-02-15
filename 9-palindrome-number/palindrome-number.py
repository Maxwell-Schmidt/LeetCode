class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        # Changes the integer to a string and checks if the string is a palindrome. If not, returns false
        if str(x)[::-1] != str(x):
            return False
        else:    
            return True
        