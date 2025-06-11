class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        s=0
        e=len(num)-1
        inv={'1':'1','0':'0','6':'9','8':'8','9':'6'}
        while s<=e:
            if num[s] in inv and num[e] in inv:
                if num[s]==inv[num[e]]:
                    s+=1
                    e-=1
                else:
                    return False
            else:
                return  False
        return True
