class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix, suffix = 0, sum(nums)
        for i in range(len(nums)):
            if prefix == suffix - nums[i]:
                return i
            prefix += nums[i]
            suffix -= nums[i]
        return -1