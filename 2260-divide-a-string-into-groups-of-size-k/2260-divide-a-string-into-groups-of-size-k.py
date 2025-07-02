class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        grps=[]
        c=''
        i=0
        n=len(s)
        while i<n:
            x=0
            while  x<k and i+x<n:
                c+=s[i+x]
                x+=1
            while len(c)<k:
                c+=fill
            grps.append(c)
            c=''
            i+=k
        return grps

