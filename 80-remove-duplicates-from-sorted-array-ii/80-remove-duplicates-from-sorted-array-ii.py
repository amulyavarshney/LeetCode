class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        copy = 0
        while i<len(nums):
            if nums[i-1] == nums[i]:
                copy += 1
                i += 1
            else:
                del nums[i-copy+1:i]
                i -= (copy-1)
                copy = 0
        del nums[i-copy+1:i]
        return len(nums)