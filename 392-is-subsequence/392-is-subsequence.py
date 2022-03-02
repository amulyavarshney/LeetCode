class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, n = 0, len(s)
        if not s:
            return True
        elif len(t) < len(s):
            return False
        for x in t:
            if s[i] == x:
                i += 1
            if i == n:
                return True
        else:
            return False