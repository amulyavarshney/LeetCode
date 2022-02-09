class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k==0:
            c = collections.Counter(nums)
            return sum([1 for x in c.values() if x>1])
        nums = set(nums)
        s = set()
        ans = 0
        for x in nums:
            if x-k in s:
                ans += 1
            if x+k in s:
                ans += 1
            s.add(x)
        return ans