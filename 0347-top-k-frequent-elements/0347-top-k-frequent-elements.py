import heapq
from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq_map = Counter(nums)
        max_heap = []

        for num, freq in freq_map.items():
            heapq.heappush(max_heap, (-freq, -num)) 

        
        top_k = []
        for _ in range(k):
            freq, num = heapq.heappop(max_heap)
            top_k.append(-num)  # Remember to negate back the number
        return top_k

        