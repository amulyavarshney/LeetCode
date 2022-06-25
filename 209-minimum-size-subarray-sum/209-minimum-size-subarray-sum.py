class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans = n+1
        start, s = 0, 0
        for i in range(n):
            s += nums[i]
            if s >= target:
                while s >= target:
                    ans = min(ans, i-start+1)
                    s -= nums[start]
                    start += 1
        return ans if ans != n+1 else 0