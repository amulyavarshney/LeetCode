# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        node = left = head
        c = 0
        while node:
            c += 1
            if c==k: left = node
            node = node.next
        c -= k
        right = head
        while c>0:
            right = right.next
            c -= 1
        left.val, right.val = right.val, left.val
        print(left.val, right.val)
        return head
            