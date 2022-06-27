# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        try:
            slow, fast = head, head.next
            while slow != fast:
                if fast is None or fast.next is None:
                    return
                slow, fast = slow.next, fast.next.next
        except:
            return
        slow = slow.next
        while head != slow:
            head, slow = head.next, slow.next
        return head
        