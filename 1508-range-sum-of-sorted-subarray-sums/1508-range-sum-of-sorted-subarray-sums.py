class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        mod = 10**9+7
        ps = []
        for i in range(n):
            ps.append(nums[i])
            for j in range(i+1, n):
                ps.append(ps[-1]+nums[j])
        ps.sort()
        pps = [0]
        for i in range(len(ps)):
            pps.append(pps[-1]+ps[i])
        return (pps[right]-pps[left-1])%mod