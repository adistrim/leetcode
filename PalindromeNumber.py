class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        Xrev = x[::-1]
        if x == Xrev:
            return True
        else:
            return False
        