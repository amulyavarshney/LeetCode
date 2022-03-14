class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return True
        x = nums[0]
        flag = 0
        for i in range(1, n):
            if x < nums[i]:
                if flag == 0:
                    flag = 1
                elif flag == -1:
                    return False
            elif x > nums[i]:
                if flag == 0:
                    flag = -1
                elif flag == 1:
                    return False
            x = nums[i]
        return True