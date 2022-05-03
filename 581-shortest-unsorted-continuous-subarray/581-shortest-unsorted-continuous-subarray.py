class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        arr = sorted(nums)
        i, j = 0, len(nums)-1
        while i<=j:
            if arr[i] == nums[i]:
                i += 1
            elif arr[j] == nums[j]:
                j -= 1
            else:
                break
        return j-i+1