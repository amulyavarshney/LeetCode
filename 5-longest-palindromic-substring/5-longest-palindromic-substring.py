class Solution:
    def longestPalindrome(self, s: str) -> str:
        def lps(i, j):
            while i>=0 and j<len(s) and s[i] == s[j]:
                i, j = i-1, j+1
            return j-i-1
        l, r = 0, 0
        for i in range(len(s)):
            x = max(lps(i,i), lps(i,i+1))
            if x > r-l:
                l = i - (x-1)//2
                r = i + x//2
        return s[l:r+1]