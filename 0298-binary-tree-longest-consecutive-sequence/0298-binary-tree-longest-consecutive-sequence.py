# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        ans=0
        def dfs(node,l):
            if not node:
                return l
            x,y=0,0
            if node.left:
                if node.val==node.left.val-1:
                    x=dfs(node.left,l+1)
                else:
                    x=dfs(node.left,0)
                    x=max(x,l)
            
            if node.right:
                if node.val==node.right.val-1:
                    y=dfs(node.right,l+1)
                else:
                    y=dfs(node.right,0)
                    y=max(y,l)
            print(node.val,x,y)
            return max(x,y,l)
        return dfs(root,0)+1
            