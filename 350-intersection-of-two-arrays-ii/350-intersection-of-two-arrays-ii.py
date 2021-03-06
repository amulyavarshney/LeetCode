class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        for x in nums1:
            d[x] = d.get(x,0) + 1
        ans = []
        for x in nums2:
            if x in d and d[x] > 0:
                ans.append(x)
                d[x] -= 1
        return ans