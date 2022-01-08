# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
​
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        leftTree,rightTree = [],[]
        if not root:
            return False
        stack = []
        stack.append(root.left)
        stack.append(root.right)
        while stack:
            p, q = stack.pop(), stack.pop()
            if p is None and q is None:
                continue
            if p is None or q is None or p.val != q.val:
                return False
            stack.append(q.left)
            stack.append(p.right)
            
            stack.append(q.right)
            stack.append(p.left)
            
        return True
        
        
        
