class Solution {
public:
    int maxArea(vector<int>& height) {
        
        int n = height.size();
        int left = 0, right = n - 1;
        int water = 0;
        
        while (left < right) {
            int width = right - left;
            int minHeight = min(height[left], height[right]);
            int curWater = minHeight * width;
            
            water = max(water, curWater);
            
            if (height[left] < height[right]){
                left++;
            } else {
                right--;
            }
            
        }
        
        return water;
    }
};