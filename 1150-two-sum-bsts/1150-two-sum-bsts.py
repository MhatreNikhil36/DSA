class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        
        def checksum(a, b, target, visited):
            if not a or not b:
                return False
            
            if (a, b) in visited:
                return False
            
            visited.add((a, b))
            
            csum = a.val + b.val
            
            if csum == target:
                return True
            
            elif csum > target:
                return (checksum(a.left, b, target, visited) or
                        checksum(a, b.left, target, visited))
            
            else:
                return (checksum(a.right, b, target, visited) or
                        checksum(a, b.right, target, visited))
        
        visited = set()
        return checksum(root1, root2, target, visited)
