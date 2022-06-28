class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = [0]*52
        for x in s:
            if x.islower():
                d[ord(x)-97] += 1
            else:
                d[ord(x)-65+26] += 1
        odd, ans = 0, 0
        for i in range(52):
            ans += d[i]
            if d[i]&1:
                odd += 1
        return ans - max(0, odd-1)