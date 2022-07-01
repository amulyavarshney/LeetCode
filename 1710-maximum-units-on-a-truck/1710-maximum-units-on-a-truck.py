class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: -x[1])
        count = 0
        for box, items in boxTypes:
            if box <= truckSize:
                count += box*items
                truckSize -= box
            else:
                count += truckSize*items
                break
        return count