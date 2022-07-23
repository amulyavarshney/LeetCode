class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        nums = list(zip(nums, range(len(nums))))
        ans = [0]*len(nums)
        def merge(l, m, r):
            j = m
            c = 0
            mergeArr = []
            while(l<m and j<r):
                if(nums[j][0] < nums[l][0]):
                    mergeArr.append(nums[j])
                    c += 1
                    j += 1
                else:
                    mergeArr.append(nums[l])
                    ans[nums[l][1]] += c
                    l += 1
            while l<m:
                mergeArr.append(nums[l])
                ans[nums[l][1]] += c
                l += 1
            while j<r:
                mergeArr.append(nums[j])
                j += 1
            return mergeArr
    
        def partition(l, r):
            if l+1>=r:
                return 
            m = l + (r-l)//2
            partition(l, m)
            partition(m, r)
            nums[l:r] = merge(l, m, r)
        partition(0, len(nums))
        return ans