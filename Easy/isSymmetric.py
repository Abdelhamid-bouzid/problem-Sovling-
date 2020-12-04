# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.boolean1(root,root)
    def boolean1(self, t1,t2):
        if not(t1) and not(t2):
            return True 
        if  not(t1) or not(t2):
            return False 
        
        l1 = t1.val==t2.val
        l2 = self.boolean1(t1.right,t2.left)
        l3 = self.boolean1(t1.left,t2.right)
        return l1 and l2 and l3
