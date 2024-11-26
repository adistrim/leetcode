class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # approach would be to 
        # ''.join(sorted(var_name)) that's how we sort a string [properly]

        s = ''.join(sorted(s))
        t = ''.join(sorted(t))

        if s == t:
            return True
        else:
            return False