class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        ans, start = 0, 0
        for i in range(1, len(nums)):
            if nums[i]-nums[i-1]>1:
                ans = max(ans, i-start)
                start = i
        return max(ans, len(nums)-start)