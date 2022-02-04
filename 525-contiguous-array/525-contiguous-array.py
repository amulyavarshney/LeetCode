class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        d = {0:-1}
        c, ans = 0, 0
        for i in range(n):
            c += 1 if nums[i]==1 else -1
            if c in d:
                ans = max(ans, i-d[c])
            else:
                d[c] = i
        return ans
        