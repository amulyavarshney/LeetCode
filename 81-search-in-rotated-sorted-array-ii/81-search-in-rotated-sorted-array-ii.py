class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        i, j = 0, len(nums)-1
        while i<=j:
            m = i + (j-i)//2
            if nums[m] == target:
                return True
            elif nums[i] <= nums[m]:
                if nums[i] <= target < nums[m]:
                    j = m-1
                else:
                    i = m+1
            else:
                if nums[m] < target <= nums[j]:
                    i = m+1
                else:
                    j = m-1
        try:
            return nums.index(target)
        except:
            return False