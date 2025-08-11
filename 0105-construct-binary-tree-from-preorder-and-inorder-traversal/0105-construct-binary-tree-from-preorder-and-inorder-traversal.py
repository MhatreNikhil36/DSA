# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder=deque(preorder)
        # print(inorder)
        parent=TreeNode(val=preorder.popleft())
        leftin=[]
        rightin=[]
        i=0
        while inorder[i]!=parent.val:
            leftin.append(inorder[i])
            i+=1
        i+=1
        while i <len(inorder):
            rightin.append(inorder[i])
            i+=1
        leftpre=[]
        rightpre=[]
        for i in range(len(preorder)):
            if i<len(leftin):
                leftpre.append(preorder[i])
            else:
                rightpre.append(preorder[i])
        if not leftpre:
            parent.left=None
        else :
            parent.left=self.buildTree(leftpre,leftin)

        if not rightpre:
            parent.right=None
        else :
            parent.right=self.buildTree(rightpre,rightin)
        return parent
            
