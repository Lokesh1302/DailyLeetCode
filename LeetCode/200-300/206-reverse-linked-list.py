# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        prev, cur, _next = None, head, None
        while cur is not None:
            _next = cur.next
            cur.next = prev
            prev = cur
            cur = _next
        return prev
