class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1, v2 = list(map(int, version1.split('.'))), list(map(int, version2.split('.')))
        n1, n2 = len(v1), len(v2)
        if n1<n2:
            v1.extend([0]*(n2-n1))
            n = n2
        else:
            v2.extend([0]*(n1-n2))
            n = n1
        for i in range(n):
            if v1[i] < v2[i]:
                return -1
            elif v1[i] > v2[i]:
                return 1
        return 0