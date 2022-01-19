class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        Find the prefix sum for each element in nums, and for each starting position in nums             find the longest subarray with maximum number of 1's using Binary Search.
        > ans = k
        > For each i in range [0..n-1]:
        > Binary search to find the rightmost index j, where subarray nums[i..j] contains 
          enough (j-i+1) ones if we flip at most k zeros.
        > ans = max(ans, j - i + 1)
        > The result is ans.
        
        TC = O(NlogN), SC = O(N)
        """
        n = len(nums)
        ps = [0]
        for p in nums:
            ps.append(ps[-1]+p)
        def binarySearch(start):
            l, r, x = start, n-1, start-1
            while l<=r:
                m = l+(r-l)//2
                z = m-start+1
                c1 = ps[m+1]-ps[start]
                if c1+k >= z:
                    x = m
                    l = m+1
                else:
                    r = m-1
            return x
        ans = k
        for i in range(n):
            j = binarySearch(i)
            ans = max(ans, j-i+1)
        return ans
            