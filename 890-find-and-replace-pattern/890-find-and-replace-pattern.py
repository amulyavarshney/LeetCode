class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        n = len(pattern)
        ans = []
        for word in words:
            d1, d2 = {}, {}
            for i in range(n):
                if d1.setdefault(pattern[i], word[i]) != word[i] or d2.setdefault(word[i], pattern[i]) != pattern[i] :
                    break
            else:
                ans.append(word)
        return ans