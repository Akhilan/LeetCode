func minPairSum(nums []int) int {
    
    sort.Ints(nums)
    
    n:= len(nums)
    result := 0
    
    for i:= 0; i < n/2 ; i++  {
        result = max(result, nums[i] + nums[n - i - 1])
    }
    return result
}