class Solution:
    def romanToInt(self, s: str) -> int:
        RomanMap={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        ans=0
        pRank=0
        s=list(s)
        while s:
            c=s.pop()
            cRank=RomanMap[c]
            if cRank<pRank:
                ans-=RomanMap[c]
            else:
                ans+=RomanMap[c]
            pRank=cRank
        return ans 
