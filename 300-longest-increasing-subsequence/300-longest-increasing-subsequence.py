class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        s = [nums[0]]
        for i in range(1, n):
            if s[-1] < nums[i]:
                s.append(nums[i])
            else:
                idx = bisect.bisect_left(s, nums[i])
                s[idx] = nums[i]
        return len(s)