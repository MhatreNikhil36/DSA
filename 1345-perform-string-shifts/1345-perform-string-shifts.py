class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        i=0
        m=len(s)
        for sp in shift:
            if sp[0]==0:
                i+=sp[1]
            else:
                i-=sp[1]
            i=i%m
        print(i)
        return(s[i:]+s[:i])
        print()
    