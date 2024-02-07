class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        cnt = Counter(s)
        s = list(s)
        s.sort(key=lambda x:(-cnt[x], x))
        return "".join(s)