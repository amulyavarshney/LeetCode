class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(collections.Counter(nums))<len(nums)