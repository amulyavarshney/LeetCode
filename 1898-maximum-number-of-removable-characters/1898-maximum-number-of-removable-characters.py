class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def isSubseq(p, s):
            i, j = 0, 0
            while i<len(p) and j<len(s):
                if p[i] == s[j]:
                    i += 1
                j += 1
            return i==len(p)
        
        l, r = 0, len(removable)
        while(l<=r):
            m = l+(r-l)//2
            seq = list(s)
            for i in range(m):
                seq[removable[i]] = '*'
            if isSubseq(p, seq):
                l = m+1
            else:
                r = m-1
        return l-1