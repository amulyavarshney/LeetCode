# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        class heapObj:
            def __init__(self, node):
                self.node = node
            def __lt__(self, other):
                return self.node.val < other.node.val
        q = []
        for l in lists:
            if l:
                heapq.heappush(q, heapObj(l))
        head = cur = ListNode()
        while q:
            node = heapq.heappop(q).node
            cur.next = node
            cur = cur.next
            node = node.next
            if node:
                heapq.heappush(q, heapObj(node))
        return head.next