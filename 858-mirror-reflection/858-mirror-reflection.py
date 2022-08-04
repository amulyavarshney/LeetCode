class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        for i in range(1, 1000):
            x, r = divmod(i*q, p)
            if r!=0:
                continue
            if x&1:
                if i&1:
                    return 1
                else:
                    return 2
            elif i&1:
                return 0
            return -1