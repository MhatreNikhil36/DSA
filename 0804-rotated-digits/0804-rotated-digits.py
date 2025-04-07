class Solution:
    def rotatedDigits(self, n: int) -> int:
        rMap={0:0,1:1,2:5,3:None,4:None,7:None,5:2,6:9,9:6,10:10,8:8}
        ans=0
        for i in range(n+1):
            if i in rMap:
                if rMap[i]!=None and rMap[i]!=i:
                    ans+=1
            
            else:
                lmin=i%10
                lmaj=i//10
                
                if rMap[lmin]!=None and rMap[lmaj]!=None:
                    rev=rMap[lmaj]*10 +rMap[lmin]
                    # print('check',i,rev,ans)
                    rMap[i]=rev
                    if i!=rev:
                        ans+=1
                    # print('check',i,rev,ans)
                else:
                    rMap[i]=None 
        return ans