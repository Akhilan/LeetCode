impl Solution {
    pub fn min_pair_sum(nums: Vec<i32>) -> i32 {
        let mut sorted_nums = nums.clone();
        sorted_nums.sort();

        // Step 2: Pair up the elements
        let n = sorted_nums.len();
        let mut result = 0;
        for i in 0..n / 2 {
        result = result.max(sorted_nums[i] + sorted_nums[n - i - 1]);
    }

    result
    }
}