class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = [[]]
        for i in range(n):
            m = len(ans)
            for j in range(len(ans)):
                ans.append(ans[j]+[nums[i]])
        return ans
            
        