class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        mod = 10**9+7
        s = sorted(set(nums1))
        ans = 0; gain = 0
        for i in range(len(nums1)):
            x = abs(nums1[i]-nums2[i])
            ans += x
            if gain < x:
                lb = bisect.bisect_left(s, nums2[i])
                if lb < len(s):
                    gain = max(gain, x-abs(s[lb]-nums2[i]))
                if lb > 0:
                    gain = max(gain, x-abs(s[lb-1]-nums2[i]))
        return (ans - gain)%mod