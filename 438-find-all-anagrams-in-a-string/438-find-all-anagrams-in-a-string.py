class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m, n = len(p), len(s)
        pp = [0]*26
        for x in p:
            pp[ord(x)-97] += 1
        if m>n:
            return []
        d = [0]*26
        for i in range(m):
            x = ord(s[i])-97
            d[x] += 1
        ans = [0] if d==pp else []
        for i in range(1, n-m+1):
            d[ord(s[i-1])-97] -= 1
            d[ord(s[i+m-1])-97] += 1
            if d==pp:
                ans.append(i)
        return ans