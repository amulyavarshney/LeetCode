class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        mod = 10**9+7
        horizontalCuts.sort()
        horizontalCuts.append(h)
        verticalCuts.sort()
        verticalCuts.append(w)
        max_h, max_w = horizontalCuts[0], verticalCuts[0]
        for i in range(1, len(horizontalCuts)):
            max_h = max(max_h, horizontalCuts[i]-horizontalCuts[i-1])
        for i in range(1, len(verticalCuts)):
            max_w = max(max_w, verticalCuts[i]-verticalCuts[i-1])
        return ((max_h%mod)*(max_w%mod))%mod