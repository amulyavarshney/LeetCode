class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        count = 0
        for i in range(n-2):
            for j in range(i+1, n-1):
                k = bisect.bisect_left(nums, nums[i] + nums[j])
                count += max(0, k-j-1)
        return count