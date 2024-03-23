# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        secondHead = self.reverseList(slow.next)
        slow.next = None

        firstHead, _next = head, None
        while firstHead is not None and secondHead is not None:
            _next = firstHead.next
            firstHead.next = secondHead
            secondHead = secondHead.next
            firstHead.next.next = _next
            firstHead = _next
        
        return head

    def reverseList(self, head):
        prev, cur, _next = None, head, None
        while cur is not None:
            _next = cur.next
            cur.next = prev
            prev = cur
            cur = _next
        return prev 
