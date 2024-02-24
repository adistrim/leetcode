class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        else:
            s = ''.join(sorted(s))
            t = ''.join(sorted(t))
            if s != t:
                return False
            else:
                return True