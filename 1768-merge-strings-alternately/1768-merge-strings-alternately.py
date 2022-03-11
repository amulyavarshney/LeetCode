class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = []
        m, n = len(word1), len(word2)
        i = 0
        while i<m and i<n:
            s.append(word1[i])
            s.append(word2[i])
            i += 1
        if i<m:
            s.extend(word1[i:])
        elif i<n:
            s.extend(word2[i:])
        return ''.join(s)