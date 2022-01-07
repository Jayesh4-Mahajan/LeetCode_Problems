# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
​
# def printNode(root,res):
#     if root:
#         res.append(root.val)
#     else:
#         return res
#     if root.left:
#         printNode(root.left,res)
#     if root.right:
#         printNode(root.right,res)
#     return res
        
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # res = []            
        # return printNode(root,res)
        
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return res
        
