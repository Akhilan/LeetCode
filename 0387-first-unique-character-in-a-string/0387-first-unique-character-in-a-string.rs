use std::collections::HashMap;

impl Solution {
    pub fn first_uniq_char(s: String) -> i32 {
        let mut char_frequency = HashMap::new();

    // Populate the frequency map
    for char in s.chars() {
        *char_frequency.entry(char).or_insert(0) += 1;
    }

    // Find the first character with a frequency of 1
    for (index, char) in s.chars().enumerate() {
        if char_frequency[&char] == 1 {
            return index as i32;
        }
    }

    // If no unique character is found, return -1
    -1
    }
}