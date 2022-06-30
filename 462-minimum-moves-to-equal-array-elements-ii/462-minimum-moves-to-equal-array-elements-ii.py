class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        l, r = 0, len(nums)-1
        c = 0
        while(l<r):
            c += nums[r]-nums[l]
            l, r = l+1, r-1
        return c