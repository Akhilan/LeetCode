func firstUniqChar(s string) int {
    charFrequency := make(map[rune]int)

	// Populate the frequency map
	for _, char := range s {
		charFrequency[char]++
	}

	// Find the first character with a frequency of 1
	for i, char := range s {
		if charFrequency[char] == 1 {
			return i
		}
	}

	// If no unique character is found, return -1
	return -1
}