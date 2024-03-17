class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        sum_map = {0: 1}  # Initialize a hashmap to store cumulative sums and their frequencies
        current_sum = 0

        for num in nums:
            current_sum += num
            complement = current_sum - k  # Calculate the complement required for the sum to be k

            if complement in sum_map:
                count += sum_map[complement]  # Add the frequency of complement sums

            sum_map[current_sum] = sum_map.get(current_sum, 0) + 1  # Update the frequency of current sum

        return count
                
        