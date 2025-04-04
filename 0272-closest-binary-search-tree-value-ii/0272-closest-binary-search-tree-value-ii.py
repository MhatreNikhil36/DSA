# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import heapq
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        minH=[]

        def trav(root):
            if not root :
                return 
            d=abs(target-root.val)
            heapq.heappush(minH,(d,root.val))
            if root.left:
                trav(root.left)
            if root.right:
                trav(root.right)
        trav(root)
        ans=[]
        while len(ans)<k:
            ans.append(heapq.heappop(minH)[1])
        return ans 


