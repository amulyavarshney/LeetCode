class Solution:
    def freqAlphabets(self, s: str) -> str:
        s = s.split('#')
        ans = []
        for x in s[:-1]:
            for i in range(len(x)-2):
                ans.append(chr(int(x[i])+96))
            if len(x)>1:
                ans.append(chr(int(x[-2:])+96))
        for x in s[-1]:
            ans.append(chr(int(x)+96))
        return ''.join(ans)