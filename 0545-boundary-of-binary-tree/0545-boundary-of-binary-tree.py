class Solution:
    def isLeaf(self, t):
        # Check if a node is a leaf (no left and right children)
        return t.left is None and t.right is None

    def addLeaves(self, res, root):
        # Recursively add leaves to the result list
        if self.isLeaf(root):
            res.append(root.val)
        else:
            if root.left:
                self.addLeaves(res, root.left)
            if root.right:
                self.addLeaves(res, root.right)

    def boundaryOfBinaryTree(self, root):
        res = []
        if not root:
            return res
        
        # Add the root if it's not a leaf
        if not self.isLeaf(root):
            res.append(root.val)
        
        # Traverse left boundary
        t = root.left
        while t:
            if not self.isLeaf(t):
                res.append(t.val)
            if t.left:
                t = t.left
            else:
                t = t.right
        
        # Add leaves in left-to-right order
        self.addLeaves(res, root)
        
        # Traverse right boundary
        s = []
        t = root.right
        while t:
            if not self.isLeaf(t):
                s.append(t.val)
            if t.right:
                t = t.right
            else:
                t = t.left
        
        # Add right boundary in reverse order
        while s:
            res.append(s.pop())
        
        return res