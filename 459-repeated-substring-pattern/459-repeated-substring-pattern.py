class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(1, len(s)):
            q, r = divmod(len(s), i)
            if r == 0 and s[:i]*q == s:
                return True
        return False