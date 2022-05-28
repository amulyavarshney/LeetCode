class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        arr = [0]*(len(nums)+1)
        for x in nums:
            arr[x] += 1
        return arr.index(0)