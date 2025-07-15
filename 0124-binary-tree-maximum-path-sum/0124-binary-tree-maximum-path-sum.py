# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        pathsums=dict()
        ans=-math.inf
        def sumUp(root):
            nonlocal ans
            if  not root:
                return
            l,r=0,0 
            if  root.left:
                l=sumUp(root.left)
            if  root.right:
                r=sumUp(root.right)
            
            val=max(root.val,r+root.val,l+root.val)
            if l+r+root.val>ans:
                ans=l+r+root.val
            if  val>ans:
                ans=val
            pathsums[root.val]=val
            return val
        sumUp(root)
        return  ans


        