# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        res = []
        if root == None:
            return res
        q = []
        q.append([root, 1])
        while len(q) != 0:
            node, dep = q.pop()
            if len(res) < dep:
                res.append([node.val])
            else:
                res[dep-1].append(node.val)
            if node.right != None:
                q.append([node.right, dep + 1])        
            if node.left != None:
                q.append([node.left, dep + 1])
        return res[::-1]
