class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:

        s=[]
        min=-inf
        for x in preorder:
            while len(s)>0  and s[-1]<x:
                min=s.pop()
            if x<=min:
                return False
            
            s.append(x)
        return True
