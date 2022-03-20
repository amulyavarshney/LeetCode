class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        d = Counter(tops + bottoms).most_common()
        if d[0][1] < n:
            return -1
        c = 0
        for i in range(n):
            if tops[i] == d[0][0]:
                pass
            elif bottoms[i] == d[0][0]:
                c += 1
            else:
                return -1
        x = 0
        for i in range(n):
            if bottoms[i] == d[0][0]:
                pass
            elif tops[i] == d[0][0]:
                x += 1
            else:
                return -1
        return min(c, x)