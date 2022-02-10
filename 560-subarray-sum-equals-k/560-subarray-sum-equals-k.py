class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ps = [0]
        for x in nums:
            ps.append(ps[-1]+x)
        d = {}
        ans = 0
        for i in range(len(ps)):
            if ps[i]-k in d:
                ans += d[ps[i]-k]
            d[ps[i]] = d.get(ps[i], 0) + 1
        return ans