func rotate(nums []int, k int)  {
    
// Calculate the effective rotation index
	k %= len(nums)

	// Reverse the entire array
	reverse(nums)

	// Reverse the first k elements
	reverse(nums[:k])

	// Reverse the remaining elements
	reverse(nums[k:])
}

func reverse(nums []int) {
	start, end := 0, len(nums)-1
	for start < end {
		nums[start], nums[end] = nums[end], nums[start]
		start++
		end--
	}
}