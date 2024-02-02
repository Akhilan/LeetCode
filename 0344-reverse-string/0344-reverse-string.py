class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        size = len(s)
		
        for i in range(size//2):
            s[i], s[-i-1] = s[-i-1], s[i]