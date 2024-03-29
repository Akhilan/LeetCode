class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        while len(s) > 1 and s[0] == s[-1]:
            s = s.strip(s[0])
        return len(s)