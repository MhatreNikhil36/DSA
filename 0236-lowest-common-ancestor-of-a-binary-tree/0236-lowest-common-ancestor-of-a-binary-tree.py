# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = None
        
        def find(root, a, b):
            nonlocal ans
            if ans is not None:
                return 0
            
            if root is None:
                return 0
            
            l = find(root.left, a, b)
            r = find(root.right, a, b)
            
            mid = 1 if root.val == a.val or root.val == b.val else 0
            
            if l + r + mid >= 2:
                ans = root
            
            return l or r or mid
        
        find(root, p, q)
        return ans