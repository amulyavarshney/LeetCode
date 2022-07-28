class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        a = sorted(nums)
        ans = 0
        for i in range(n):
            if a[i] != nums[i]:
                ans -= i
                break
        for j in range(n-1, -1, -1):
            if a[j] != nums[j]:
                ans += j+1
                break
        return max(ans, 0)