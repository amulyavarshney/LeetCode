class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = collections.Counter(magazine)
        for x in ransomNote:
            if d.get(x,0)>0:
                d[x] -= 1
            else:
                return False
        return True