class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        dict_p, dict_s = [0]*26, [0]*26
        for i in range(len(p)):
            dict_p[ord(p[i])-97] += 1
            dict_s[ord(s[i])-97] += 1
        ans = []
        for i in range(len(p), len(s)):
            if dict_s == dict_p:
                ans.append(i-len(p))
            dict_s[ord(s[i-len(p)])-97] -= 1
            dict_s[ord(s[i])-97] += 1
        if dict_s == dict_p:
            ans.append(len(s)-len(p))
        return ans