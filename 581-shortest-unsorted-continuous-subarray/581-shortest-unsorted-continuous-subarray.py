class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left, stack = n, []
        for i in range(n):
            while(stack and nums[stack[-1]] > nums[i]):
                left = min(left, stack.pop())
            stack.append(i)
        right, stack = 0, []
        for i in range(n-1, -1, -1):
            while(stack and nums[stack[-1]] < nums[i]):
                right = max(right, stack.pop())
            stack.append(i)
        return right-left+1 if right>left else 0