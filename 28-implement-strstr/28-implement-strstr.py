class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # try:
        #     return haystack.index(needle)
        # except:
        #     return -1
        for i in range(len(haystack)-len(needle)+1):
            for j in range(len(needle)):
                if haystack[i+j] != needle[j]:
                    break
            else:
                return i
        return -1