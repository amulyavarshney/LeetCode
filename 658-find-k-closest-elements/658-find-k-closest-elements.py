class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        l, r = 0, n-1
        while(l<=r):
            m = l + (r-l)//2
            if arr[m] >= x:
                r = m-1
            else:
                l = m+1
        ans1, ans2 = [], []
        while k>0:
            if r>=0 and l<n:
                if abs(x-arr[r]) <= abs(x-arr[l]):
                    ans1.append(arr[r])
                    r -= 1
                else:
                    ans2.append(arr[l])
                    l += 1
            elif r>=0:
                ans1.append(arr[r])
                r -= 1
            else:
                ans2.append(arr[l])
                l += 1
            k -= 1
        return ans1[::-1] + ans2