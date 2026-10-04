# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        res = []

        def postOrder(root):
            if not root:
                return
            
            postOrder(root.left)
            postOrder(root.right)
            res.append(root.val)
        
        postOrder(root)
        return res