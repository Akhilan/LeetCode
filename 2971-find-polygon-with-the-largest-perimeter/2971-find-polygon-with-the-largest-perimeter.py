class Solution(object):
    def largestPerimeter(self, A):
        """
        :type nums: List[int]
        :rtype: int
        """
        A.sort()
        cur = sum(A)
        while A and cur <= A[-1] * 2:
            cur -= A.pop()
        return sum(A) if len(A) > 2 else -1
