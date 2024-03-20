# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        secondListHead, secondListTail = list2, list2
        while secondListTail.next is not None:  # We are aware that secondList is not null from constraints
            secondListTail = secondListTail.next
        
        firstListHead, firstListIndex = list1, 1
        pointer1, pointer2 = firstListHead, firstListHead

        while firstListIndex != (b + 1):
            firstListHead = firstListHead.next
            firstListIndex += 1

            if firstListIndex == a:
                pointer1 = firstListHead
                    
        pointer2 = firstListHead 

        pointer1.next = secondListHead
        secondListTail.next = pointer2.next

        return list1

        
