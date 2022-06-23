class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        day = 0
        heap = []
        for i in range(len(courses)):
            if day <= courses[i][1] - courses[i][0]:
                heapq.heappush(heap, -courses[i][0])
                day += courses[i][0]
            elif heap:
                x = -heapq.heappop(heap)
                if x > courses[i][0]:
                    day += courses[i][0] - x
                    heapq.heappush(heap, -courses[i][0])
                else:
                    heapq.heappush(heap, -x)
        return len(heap)