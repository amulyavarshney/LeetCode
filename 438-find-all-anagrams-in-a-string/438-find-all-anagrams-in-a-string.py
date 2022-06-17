class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(p)
        d1, d2 = [0]*26, [0]*26
        ans = []
        for x in p:
            d1[ord(x)-97] += 1
        for i in range(len(s)):
            if sum(d2)>=sum(d1):
                d2[ord(s[i-n])-97] -= 1
            d2[ord(s[i])-97] += 1
            if d1 == d2:
                ans.append(i-n+1)
        return ans