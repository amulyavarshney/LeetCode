# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        i = 0
        while i<=n:
            m = i + (n-i)//2
            if isBadVersion(m) == True:
                n = m-1
            else:
                i = m+1
        return i