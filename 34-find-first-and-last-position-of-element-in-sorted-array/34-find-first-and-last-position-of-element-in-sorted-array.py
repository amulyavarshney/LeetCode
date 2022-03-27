class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bs(i, j):
            while i<=j:
                m = i+(j-i)//2
                if nums[m] >= target:
                    j = m-1
                else:
                    i = m+1
            return i
        def bs2(i, j):
            while i<=j:
                m = i+(j-i)//2
                if nums[m] > target:
                    j = m-1
                else:
                    i = m+1
            return j
        n = len(nums)
        l, r = bs(0, n-1), bs2(0, n-1)
        return [l,r] if l<=r else [-1,-1]