class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        for e in arr:
            heapq.heappush(heap, (abs(x-e), e))
        ans = []
        while k>0:
            ans.append(heapq.heappop(heap)[1])
            k -= 1
        return sorted(ans)