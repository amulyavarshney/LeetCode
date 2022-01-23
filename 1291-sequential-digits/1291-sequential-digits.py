class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        t = [1, 12, 123, 1234, 12345, 123456, 1234567, 12345678, 123456789, float("inf")]
        lx = -1
        for i in range(10):
            if t[i] > low:
                x = t[i-1]
                break
        ans = []
        k = len(str(x))
        z = int('1'*k)
        i = 9-k
        while x<=high:
            if x >= low:
                ans.append(x)
            if i:
                x += z
                i -= 1
            else:
                x = t[k]
                k += 1
                z = int('1'*k)
                i = 9-k
        return ans
            