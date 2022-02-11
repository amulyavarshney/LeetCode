class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        start = 0; m = 0
        for i in range(len(s)):
            if s[i] in d and d[s[i]] >= start:
                start = d[s[i]] + 1
            m = max(m, i-start+1)
            d[s[i]] = i
        return m