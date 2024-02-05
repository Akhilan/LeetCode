class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        
        left, right = 0, n-1
        water = 0
        
        
        while left < right:
            width = right - left
            height_min = min(height[left], height[right])
            current_water = width * height_min
            
            water = max(water, current_water)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return water
        