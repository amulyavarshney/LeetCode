class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        d1, d2, d3, d4 = Counter(nums1), Counter(nums2), Counter(nums3), Counter(nums4)
        d12, d34 = Counter(), Counter()
        for i in d1:
            for j in d2:
                d12[i+j] += d1[i]*d2[j]
        for i in d3:
            for j in d4:
                d34[i+j] += d3[i]*d4[j]
        c = 0
        for i in d12:
            if -i in d34:
                c += d12[i]*d34[-i]
        return c