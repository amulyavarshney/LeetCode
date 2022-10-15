class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @lru_cache(None)
        def counter(start, last_ch, last_cnt, k_left):
            if(k_left<0):
                return float("inf")
            if(len(s)-start<=k_left):
                return 0
            if(s[start] == last_ch):
                inc = 1 if last_cnt == 1 or last_cnt == 9 or last_cnt == 99 else 0
                return inc + counter(start+1, last_ch, last_cnt+1, k_left)
            else:
                keep_ch = 1 + counter(start+1, s[start], 1, k_left)
                delete_ch = counter(start+1, last_ch, last_cnt, k_left-1)
                return min(keep_ch, delete_ch)
        return counter(0, '', 0, k)