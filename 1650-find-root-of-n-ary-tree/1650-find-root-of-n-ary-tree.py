"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        ind=dict()
        for x in tree:
            if x not in ind:
                ind[x]=0
            for y in x.children:
                if y not in ind:
                    ind[y]=0
                ind[y]+=1
        print(ind)

        for x in ind:
            if ind[x]==0:
                return x 
        return -1