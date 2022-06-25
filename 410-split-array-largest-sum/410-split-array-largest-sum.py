class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        l, r = max(nums), sum(nums)
        while(l<=r):
            mid = l + (r-l)//2
            s, c = 0, 1
            for x in nums:
                s += x
                if s > mid:
                    c += 1
                    s = x
            if c <= m:
                r = mid-1
            else:
                l = mid+1
        return r+1