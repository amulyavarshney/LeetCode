class Solution:
    def reverseWords(self, s: str) -> str:
        def rev(s):
            s = list(s)
            i, j = 0, len(s)-1
            while i<j:
                s[i], s[j] = s[j], s[i]
                i, j = i+1, j-1
            return ''.join(s)
        return ' '.join([rev(x) for x in s.split()])