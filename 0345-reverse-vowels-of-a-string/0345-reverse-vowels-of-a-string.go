func reverseVowels(s string) string {
    vowels := map[rune]bool{'a': true, 'e': true, 'i': true, 'o': true, 'u': true, 'A': true, 'E': true, 'I': true, 'O': true, 'U': true}
	sBytes := []rune(s)
	left, right := 0, len(sBytes)-1

	for left < right {
		for left < right && !vowels[sBytes[left]] {
			left++
		}
		for left < right && !vowels[sBytes[right]] {
			right--
		}
		if left < right {
			sBytes[left], sBytes[right] = sBytes[right], sBytes[left]
			left++
			right--
		}
	}
	return string(sBytes)
}