class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        ans = []
        def backtrack(cur, s, i):
            if s == target:
                ans.append(cur[:])
                return
            if s > target:
                return 
            for j in range(i, n):
                if s < target:
                    backtrack(cur+[nums[j]], s+nums[j], j)
                else:
                    backtrack(cur, s, j+1)
        backtrack([], 0, 0)
        return ans