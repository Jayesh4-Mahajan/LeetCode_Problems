# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        
        def PathSum(root,targetSum):
            if root is None:
                return False
            if root.left is None and root.right is None:
                if targetSum == root.val:
                    return True
                else:
                    return False
            return PathSum(root.left,targetSum-root.val) or PathSum(root.right,targetSum-root.val)
        
        return PathSum(root,targetSum)
                
