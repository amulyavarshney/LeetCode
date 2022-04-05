class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high-low)//2 if low&1==0 and high&1==0 else (high-low)//2+1