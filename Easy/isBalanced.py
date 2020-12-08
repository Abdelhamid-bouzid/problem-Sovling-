# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        
        if root==None:
            return True
        
        Hl = self.height(root.left)
        Hr = self.height(root.right)
        
        if (abs(Hr-Hl) <=1) and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        else:
            return False
        
    def height(self,root): 
 
        if root is None: 
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1
