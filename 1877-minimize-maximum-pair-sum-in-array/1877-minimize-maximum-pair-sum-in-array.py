class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        
        result = 0
        
        for i in range(n//2):
            result = max(result, nums[i] + nums[n - i - 1])
        
        return result