class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        d = {}
        for i in range(n):
            d[s[i]] = i
        c = 0
        start = 0
        ans = []
        for i in range(n):
            if i>c:
                ans.append(c-start+1)
                start = i
            c = max(c, d[s[i]])
        return ans+[c-start+1]