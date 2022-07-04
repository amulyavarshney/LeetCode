class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        ps = [0]
        for x in nums:
            ps.append(ps[-1]+x)
        d = {}
        start, ans = 0, 0
        for i in range(len(nums)):
            if nums[i] in d:
                start = max(start, d[nums[i]] + 1)
            d[nums[i]] = i
            ans = max(ans, ps[i+1]-ps[start])
        return ans