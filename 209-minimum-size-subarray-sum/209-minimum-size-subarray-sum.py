class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ps = [0]
        for x in nums:
            ps.append(ps[-1]+x)
        if ps[-1] < target:
            return 0
        ans = n
        for i in range(n):
            l, r = i+1, n
            while(l<r):
                mid = l + (r-l)//2
                if ps[mid]-ps[i] >= target:
                    r = mid
                else:
                    l = mid+1
            if ps[r] - ps[i] >= target:
                ans = min(ans, r-i)
        return ans