impl Solution {
    pub fn max_area(height: Vec<i32>) -> i32 {
        let mut left = 0;
    let mut right = height.len() - 1;
    let mut max_water = 0;

    while left < right {
        // Calculate the width between the two pointers
        let width = (right - left) as i32;

        // Calculate the height of the container (minimum height of the two lines)
        let h = height[left].min(height[right]);

        // Calculate the area and update max_water if the current area is greater
        let current_water = width * h;
        max_water = max_water.max(current_water);

        // Move the pointers towards each other
        if height[left] < height[right] {
            left += 1;
        } else {
            right -= 1;
        }
    }

    max_water
    }
}