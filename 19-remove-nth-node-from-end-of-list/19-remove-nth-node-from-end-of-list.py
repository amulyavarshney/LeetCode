# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        def rev(head):
            prev, cur = head, head.next
            while cur:
                prev.next, cur.next = cur.next, head
                head, cur = cur, prev.next
            return head
        head = cur = rev(head)
        if n == 1:
            head = head.next
            return rev(head)
        while n-2:
            cur = cur.next
            n -= 1
        cur.next = cur.next.next
        return rev(head)