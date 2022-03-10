# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        h1, h2, cur = l1, l2, head
        carry = 0
        while h1 and h2:
            carry, val = divmod(h1.val+h2.val+carry, 10)
            cur.next = ListNode(val)
            h1, h2, cur = h1.next, h2.next, cur.next
        while h1:
            carry, val = divmod(h1.val+carry, 10)
            cur.next = ListNode(val)
            h1, cur = h1.next, cur.next
        while h2:
            carry, val = divmod(h2.val+carry, 10)
            cur.next = ListNode(val)
            h2, cur = h2.next, cur.next
        if carry:
            cur.next = ListNode(carry)
        return head.next