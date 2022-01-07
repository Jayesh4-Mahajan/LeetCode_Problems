# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
​
def findIndex(arr, val):
    for k, v in enumerate(arr):
        if v == arr:
            return k
    return None
​
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        mp = {}
        preIdx = 0
        
        for k, v in enumerate(inorder):
            mp[v] = k
            
        def treeBuild(p, mp, preIdx, start, end):            
            curr = p[preIdx]   
            node, idx = TreeNode(curr), mp[curr]
            preIdx += 1
            if idx > start:
                node.left = treeBuild(p, mp, preIdx, start, idx-1)
            if idx < end:
                node.right = treeBuild(p, mp, preIdx + idx - start, idx+1, end)
            
            return node
        
        return treeBuild(preorder, mp, 0, 0, len(preorder)-1)
