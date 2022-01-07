# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
def inOrder(root,res):
    if root.left:
        inOrder(root.left, res)
    if root:
        res.append(root)
    if root.right:
        inOrder(root.right, res)
    return res
​
def preOrder(root, res):
    if root:
        res.append(root.val)
    if root.left:
        preOrder(root.left, res)
    if root.right:
        preOrder(root.right, res)
    return res
​
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        inn = []
        pre = []
        inn = inOrder(root, inn)
        pre = preOrder(root, pre)
        mp = {}
        for k, v in enumerate(inn):
            mp[v.val] = k
        pIdx = mp[p.val]
        qIdx = mp[q.val]
        for r in pre:
            rootIdx = mp[r]
            if (pIdx <= rootIdx <= qIdx) or (qIdx <= rootIdx <= pIdx):
                return inn[rootIdx]
        
        
        
            
        
