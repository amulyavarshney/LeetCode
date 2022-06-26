class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        ans, sub = float("inf"), 0
        for i in range(n):
            if i<n-k:
                sub += cardPoints[i]
            else:
                ans = min(ans, sub)
                sub += cardPoints[i] - cardPoints[i-n+k]
        ans = min(ans, sub)
        return sum(cardPoints)-ans