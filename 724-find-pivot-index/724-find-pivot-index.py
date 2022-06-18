class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix, s = 0, sum(nums)
        for i in range(len(nums)):
            if prefix == s - prefix - nums[i]:
                return i
            prefix += nums[i]
        return -1