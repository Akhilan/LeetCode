func maxArea(height []int) int {
    n := len(height)
	left, right := 0, n-1
	maxWater := 0

	for left < right {
		// Calculate the width between the two pointers
		width := right - left

		// Calculate the height of the container (minimum height of the two lines)
		h := min(height[left], height[right])

		// Calculate the area and update maxWater if the current area is greater
		currentWater := width * h
		maxWater = max(maxWater, currentWater)

		// Move the pointers towards each other
		if height[left] < height[right] {
			left++
		} else {
			right--
		}
	}

	return maxWater
}