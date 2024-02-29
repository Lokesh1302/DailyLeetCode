# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        _queue = Queue()
        _queue.put(root)
        level = 1
        while(_queue.qsize() > 0):
            size = _queue.qsize()
            even_prev_val = float("inf")
            odd_prev_val = float("-inf") 
            for index in range(size):
                cur = _queue.get()
                if (level % 2 == 0 and cur.val % 2 == 0 
                and even_prev_val > cur.val) or (level % 2 == 1 and cur.val % 2 == 1 
                and odd_prev_val < cur.val):
                    odd_prev_val = cur.val
                    even_prev_val = cur.val
                    if cur.left is not None:
                        _queue.put(cur.left)
                    if cur.right is not None:
                        _queue.put(cur.right)
                else:
                    return False
            level += 1
            
        return True

    # Even Decreasing Order
    # Odd Increasing Order
