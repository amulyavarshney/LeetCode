class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        nums = nums+[float("inf")]
        ans = []
        start = 0
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]+1:
                if start == i-1:
                    ans.append(str(nums[start]))
                    start = i
                else:
                    ans.append(str(nums[start])+"->"+str(nums[i-1]))
                    start = i
        return ans