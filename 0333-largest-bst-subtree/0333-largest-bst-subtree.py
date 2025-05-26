import math
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        res = [0]  # Mutable container to store max BST size

        def trav(node):
            """
            Returns (is_bst, size, min_val, max_val)
            """
            if not node:
                return True, 0, math.inf, -math.inf

            left_is_bst, left_size, left_min, left_max = trav(node.left)
            right_is_bst, right_size, right_min, right_max = trav(node.right)

            if left_is_bst and right_is_bst and left_max < node.val < right_min:
                curr_size = left_size + right_size + 1
                res[0] = max(res[0], curr_size)
                print(f"Node {node.val} forms BST. Size = {curr_size}, Updated res = {res[0]}")
                return True, curr_size, min(node.val, left_min), max(node.val, right_max)
            else:
                print(f"Node {node.val} does NOT form BST. Left_is_bst={left_is_bst}, Right_is_bst={right_is_bst}")
                return False, 0, 0, 0

        trav(root)
        return res[0]
