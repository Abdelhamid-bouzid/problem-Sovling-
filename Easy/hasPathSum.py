# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root==None:
            return False
        
        sum-=root.val
        if sum==0 and self.isleaf(root):
            return True
        
        return self.hasPathSum(root.left,sum) or self.hasPathSum(root.right,sum)
    
    def isleaf(self, root):
        if not(root.left) and not(root.right):
            return True
