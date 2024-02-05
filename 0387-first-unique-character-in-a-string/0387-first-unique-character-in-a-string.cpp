class Solution {
public:
    int firstUniqChar(string s) {
        std::unordered_map<char, int> charFrequency;

    // Populate the frequency map
    for (char c : s) {
        charFrequency[c]++;
    }

    // Find the first character with a frequency of 1
    for (int i = 0; i < s.length(); ++i) {
        if (charFrequency[s[i]] == 1) {
            return i;
        }
    }

    // If no unique character is found, return -1
    return -1;
    }
};