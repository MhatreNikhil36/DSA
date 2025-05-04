# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import OrderedDict
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        table={}
        def dfs(root,level,depth):
            if not root :
                return
            if level not in table:
                table[level]={}
            if depth not in table[level]:
                table[level][depth]=[]
            table[level][depth].append(root.val)
            if root.left:
                dfs(root.left,level-1,depth+1)
            if root.right:
                dfs(root.right,level+1,depth+1)
        dfs(root,0,0)
        ans=[]
        while table:
            level=min(table)
            arr=[]
            while table[level]:
                cd=min(table[level])
                arr+=table[level][cd]
                del table[level][cd]    
            del table[level]
            ans.append(arr)
        return ans 

                
