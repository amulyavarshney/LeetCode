class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d = [0]*26
        for x in t:
            d[ord(x)-97] += 1
        for x in s:
            d[ord(x)-97] -= 1
        return chr(d.index(1)+97)