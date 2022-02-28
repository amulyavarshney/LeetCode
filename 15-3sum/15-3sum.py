class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = set()
        for i in range(n-1):
            d = set()
            for j in range(i+1,n):
                if -nums[i]-nums[j] in d:
                    ans.add(tuple(sorted([nums[i], -nums[i]-nums[j], nums[j]])))
                d.add(nums[j])
        return ans