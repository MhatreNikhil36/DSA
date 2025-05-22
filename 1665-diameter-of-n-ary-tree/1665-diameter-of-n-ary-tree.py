# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def diameter(self, root: 'Node') -> int:
        self.ans = 0

        def dfs(node):
            # returns height of subtree rooted at node
            if not node:
                return 0
            max1, max2 = 0, 0
            for c in node.children:
                h = dfs(c)
                if h > max1:
                    max1, max2 = h, max1
                elif h > max2:
                    max2 = h
            # update diameter: the two tallest child-subtrees passing through this node
            self.ans = max(self.ans, max1 + max2)
            # height of this node is tallest child + 1
            return max1 + 1

        dfs(root)
        return self.ans
