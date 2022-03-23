class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        c = 0
        while startValue != target:
            if target&1:
                if target > startValue:
                    c += 1
                    target  += 1
                else:
                    c += startValue - target
                    target = startValue
            else:
                if target > startValue:
                    c += 1
                    target //= 2
                else:
                    c += startValue - target
                    target = startValue
        return c