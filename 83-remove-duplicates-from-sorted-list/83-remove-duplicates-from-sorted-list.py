# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        cur = head.next
        while cur and head.val == cur.val:
            head, cur = head.next, cur.next
        prev = head
        while cur:
            if prev.val == cur.val:
                prev.next = cur.next
            else:
                prev = prev.next
            cur = cur.next
        return head