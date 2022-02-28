class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = nums[0]
        c = 0
        for x in nums:
            if ans == x:
                c += 1
            else:
                if c != 0:
                    c -= 1
                else:
                    ans = x
                    c = 1
        return ans