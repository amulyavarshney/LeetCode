class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        while i<j:
            if s[i] == s[j]:
                i, j = i+1, j-1
            else:
                break
        l, r = i, j-1
        while l<r:
            if s[l] == s[r]:
                l, r = l+1, r-1
            else:
                break
        else:
            return True
        l, r = i+1, j
        while l<r:
            if s[l] == s[r]:
                l, r = l+1, r-1
            else:
                break
        else:
            return True
        return False