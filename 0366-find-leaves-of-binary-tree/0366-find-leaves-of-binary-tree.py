# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isleaf(self,root):
        if not root:
            return False
        if not root.left  and not root.right:
            return True
        return False
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[]
        
        def removeleaf(node,leaf):
            if not node :
                return
            if self.isleaf(node.left):
                leaf.append(node.left.val)
                node.left=None
            else:
                removeleaf(node.left,leaf)

            if self.isleaf(node.right):
                leaf.append(node.right.val)
                node.right=None
            else:
                removeleaf(node.right,leaf)
        
        while not self.isleaf(root):
            l=[]
            removeleaf(root,l)
            ans.append(l)
        ans.append([root.val])
        return ans 
    

        