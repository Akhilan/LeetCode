class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_frequency = {}

        # Iterate through the string to populate the dictionary
        for char in s:
            if char in char_frequency:
                char_frequency[char] += 1
            else:
                char_frequency[char] = 1

        # Iterate through the string again to find the first character with a frequency of 1
        for i in range(len(s)):
            if char_frequency[s[i]] == 1:
                return i

        # If no unique character is found, return -1
        return -1