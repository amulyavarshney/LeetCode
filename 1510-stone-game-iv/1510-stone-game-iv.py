
from functools import lru_cache
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        @lru_cache(None)
        def dfs(x):
            if x==0:
                return False
            sqrt = int(x**0.5)
            for i in range(1, sqrt+1):
                if not dfs(x-i*i):
                    return True
            return False
        return dfs(n)