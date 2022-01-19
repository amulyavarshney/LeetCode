class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        TC = O(N), SC = O(N)
        """
        d = {}
        for i, e in enumerate(nums):
            if target - e in d:
                return [d[target-e], i]
            d[e] = i