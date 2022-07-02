class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        l, r = 0, len(nums)-1
        while(l<=r):
            m = l+(r-l)//2
            if m>0 and nums[m] == nums[m-1]:
                if (m-1)&1:
                    r = m-1
                else:
                    l = m+1
            elif m+1<len(nums) and nums[m] == nums[m+1]:
                if m&1:
                    r = m-1
                else:
                    l = m+1
            else:
                return nums[m]