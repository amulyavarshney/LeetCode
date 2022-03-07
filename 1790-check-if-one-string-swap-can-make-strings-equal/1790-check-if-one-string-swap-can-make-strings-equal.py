class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        c = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                c += 1
                if c == 1:
                    x, y = s1[i], s2[i]
                elif c == 2:
                    if s1[i]!=y or s2[i]!=x:
                        return False
                elif c>2:
                    return False
        return False if c==1 else True