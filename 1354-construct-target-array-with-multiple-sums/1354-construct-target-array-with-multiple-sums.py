class Solution:
    def isPossible(self, target: List[int]) -> bool:
        s = sum(target)
        target = [-x for x in target]
        heapq.heapify(target)
        while True:
            x = -heapq.heappop(target)
            s -= x
            if x == 1 or s == 1:
                return True
            if x < s or s == 0 or x%s == 0:
                return False
            x %= s
            s += x
            heapq.heappush(target, -x)