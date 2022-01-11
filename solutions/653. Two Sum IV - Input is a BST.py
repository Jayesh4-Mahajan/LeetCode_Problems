# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
​
#  Solution 1:
​
# def inOrder(root, res):
#     if root.left:
#         inOrder(root.left, res)
#     if root:
#         res.append(root.val)
#     if root.right:
#         inOrder(root.right, res)
#     return res
​
# class Solution:
#     def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
#         if not root: return False
#         res = []
#         res = inOrder(root, res)
#         print(res)
#         c1 = 0
#         c2 = len(res) - 1
#         while c1 < c2:
#             v = res[c1]+res[c2]
#             if v == k:
#                 return True
#             elif v < k:
#                 c1 += 1
#             else:
#                 c2 -= 1
#         return False
            
#     Solution 2: Using HashMap
    
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def dfs(root, seen):
            if not root: return False
            complement = k - root.val
            if complement in seen:
                return True
            seen.add(root.val)
            return dfs(root.left, seen) or dfs(root.right, seen)
        
        return dfs(root, set())
