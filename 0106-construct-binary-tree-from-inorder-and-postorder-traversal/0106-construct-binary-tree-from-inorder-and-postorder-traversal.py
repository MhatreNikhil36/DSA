class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None

        idx_map = {val: i for i, val in enumerate(inorder)}
        post_idx = len(postorder) - 1

        def helper(l, r):
            nonlocal post_idx
            if l > r:
                return None
            val = postorder[post_idx]
            post_idx -= 1
            root = TreeNode(val)
            m = idx_map[val]
            root.right = helper(m + 1, r)
            root.left  = helper(l, m - 1)
            return root

        return helper(0, len(inorder) - 1)
