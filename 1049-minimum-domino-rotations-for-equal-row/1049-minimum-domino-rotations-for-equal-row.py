class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n=len(tops)
        c=[]
        for i in range(n-1):
            a,b=tops[i],bottoms[i]
            x,y=tops[i+1],bottoms[i+1]
            cc=[]
            if a in {x,y}:
                if not c:
                    cc.append(a)
                else:
                    if a in c[-1]:
                        cc.append(a)
            if  b in {x,y}:
                if not c:
                    cc.append(b)
                else:
                    if b in c[-1]:
                        cc.append(b)
            if len(cc)==0:
                return -1
            c.append(cc)
        i=0
        ni=0
        ans=math.inf
        print(c)
        for op in c[-1]:
            mc=op
            for x in tops:
                if  x!=mc:
                    i+=1
            for y in bottoms:
                if y!=mc:
                    ni+=1
            ans=min(ans, min(i,ni))
        return ans