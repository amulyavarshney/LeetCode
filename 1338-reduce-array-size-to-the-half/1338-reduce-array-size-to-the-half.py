class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        d = {}
        for x in arr:
            d[x] = d.get(x, 0) + 1
        c, s = 0, (len(arr)+1)//2
        for x in sorted(d.values(), reverse=True):
            c += 1
            s -= x
            if s<=0:
                return c