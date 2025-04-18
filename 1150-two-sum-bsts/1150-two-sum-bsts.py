# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        look=set()
        build=1
        def trav(root):
            if not root :
                return
            if build:
                look.add(target-root.val)
                if root.right:
                     trav(root.right)
                if root.left:
                    trav(root.left)
            if build==0:
                print(root.val)
                if root.val in look:
                    return True 
                x,y=False,False
                if root.left:
                    x= trav(root.left)
                if root.right:
                    y=trav(root.right)
                return x or y 
        trav(root1)
        build=0
        print(look)
        ans=trav(root2)
        if ans==True:
            return ans 
        return False
        

        