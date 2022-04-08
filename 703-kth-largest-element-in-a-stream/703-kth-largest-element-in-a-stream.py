class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.largest = sorted(nums, reverse=True)[:k]
        self.k = k

    def add(self, val: int) -> int:
        if len(self.largest) < self.k or val >= self.largest[self.k-1]:
            bisect.insort(self.largest, val, key=lambda x:-x)
        if len(self.largest) > self.k:
            self.largest.pop()
        return self.largest[self.k-1]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)