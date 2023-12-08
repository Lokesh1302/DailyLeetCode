# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result = ""

    def tree2str(self, root: Optional[TreeNode]) -> str:
        self.inorder(root)
        return self.result

    def inorder(self, root):
        if root is None:
            return

        self.result += str(root.val)
        if root.left is None and root.right is None:
            return
        
        self.result += "("
        self.inorder(root.left)
        self.result += ")"
        
        if root.right is not None:
            self.result += "("
            self.inorder(root.right)
            self.result += ")"
