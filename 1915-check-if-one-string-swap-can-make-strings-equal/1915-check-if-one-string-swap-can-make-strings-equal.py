from collections import Counter
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        n=len(s1)
        m=len(s2)
        if n!=m:
            return False
        
        strc1=dict(Counter(s1))
        strc2=dict(Counter(s2))
        if strc1!=strc2:
            return False 
        # return True
        miss=0
        for i in range(n):
            if s1[i]!=s2[i]:
                miss+=1
            if miss>2:
                return False
        return True 