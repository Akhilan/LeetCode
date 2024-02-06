class Solution {
public:
void reverse(vector<int>& nums, int start, int end) {
    while (start < end) {
        swap(nums[start], nums[end]);
        start++;
        end--;
    }
}

void rotate(vector<int>& nums, int k) {
    // Calculate the effective rotation index
    k %= nums.size();

    // Reverse the entire array
    reverse(nums, 0, nums.size() - 1);

    // Reverse the first k elements
    reverse(nums, 0, k - 1);

    // Reverse the remaining elements
    reverse(nums, k, nums.size() - 1);
}
};