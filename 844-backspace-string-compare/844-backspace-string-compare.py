class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        a, b = [], []
        for x in s:
            if x == '#':
                if len(a)>0:
                    a.pop()
            else:
                a.append(x)
        for x in t:
            if x == '#':
                if len(b)>0:
                    b.pop()
            else:
                b.append(x)
        return a == b