class Solution(object):
    def maxSubarrayLength(self, A, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = Counter()
        res = i = 0
        for j in range(len(A)):
            count[A[j]] += 1
            while count[A[j]] > k:
                count[A[i]] -= 1
                i += 1
            res = max(res, j - i + 1)
        return res