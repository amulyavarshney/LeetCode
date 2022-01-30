class Solution:
    def trap(self, a: List[int]) -> int:
        i, j = 0, len(a)-1
        left, right = a[i], a[j]
        c = 0
        while i <= j:
            left, right = max(left, a[i]), max(right, a[j])
            if left <= right:
                c += left - a[i]
                i += 1
            else:
                c += right - a[j]
                j -= 1
        return c