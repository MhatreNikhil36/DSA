"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        depths=dict()
        def dep(node,d):
            if node.children==[]:
                depths[node]=[d,0,0]
                return d
            d1=0
            d2=0
            for x in node.children:
                h=dep(x,d+1)
                if h>=d1:
                    d2=d1
                    d1=h
                if h<d1 and h>d2:
                    d2=h
            depths[node]=[d,d1,d2]
            return max(d1,d2)
        ans=0
        dep(root,0)
        print(depths)
        for x in depths:
            ans=max(ans,depths[x][1]+depths[x][2]-(2*depths[x][0]))
        return ans 
        