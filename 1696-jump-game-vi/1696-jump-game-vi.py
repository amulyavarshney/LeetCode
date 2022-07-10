class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [-float("inf")]*n
        dp[0] = nums[0]
        queue = collections.deque([(dp[0], 0)])
        countAdded, countRemoved = 1, 0
        for i in range(1, n):
            dp[i] = max(dp[i], dp[queue[0][1]]+nums[i])
            if countAdded-countRemoved >= k:
                if queue and queue[0][1] == countRemoved:
                    queue.popleft()
                countRemoved += 1
            while queue and queue[-1][0] <= dp[i]:
                queue.pop()
            queue.append((dp[i], i))
            countAdded += 1
        return dp[-1]
        