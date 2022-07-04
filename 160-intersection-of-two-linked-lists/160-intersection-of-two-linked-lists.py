# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        h1, h2 = headA, headB
        while h1 != h2:
            h1 = headB if h1 == None else h1.next
            h2 = headA if h2 == None else h2.next
        return h1