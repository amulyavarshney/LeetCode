class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        For each element in nums, try to find the longest subarray using sliding window.
        If #0 in (nums[left] ~ nums[right]) <= K, we continue to increment j. else if #0 in             (nums[left] ~ nums[right]) > K, we increment left (as well as right).
        
        TC = O(n), SC = O(1)
        """
        start, c, m = 0, 0, 0
        for i in range(len(nums)):
            if nums[i] == 0:
                c += 1
            while c > k:
                if nums[start] == 0:
                    c -= 1
                start += 1
            m = max(m, i-start+1)
        return m