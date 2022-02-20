class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        ans = intervals[0]
        c = 1
        for i in range(1, len(intervals)):
            if intervals[i][0] == ans[0] and intervals[i][1] >= ans[1]:
                ans = intervals[i]
            elif intervals[i][1] > ans[1]:
                ans = intervals[i]
                c += 1
        return c