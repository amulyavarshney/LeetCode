class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        left, right = [1]*n, [1]*n
        for i in range(1, n):
            if ratings[i-1] < ratings[i]:
                left[i] = left[i-1] + 1
            j = n-1-i
            if ratings[j] > ratings[j+1]:
                right[j] = right[j+1] + 1
        return sum([max(left[i], right[i]) for i in range(n)])
        
                
            