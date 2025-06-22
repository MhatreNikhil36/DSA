class Solution:
    def numWays(self, n: int, k: int) -> int:
        
        if n==1:
            return k
        
        if n==2:
            return k*k

        ans=[0 for i in range(n+1)]
        ans[1]=k
        ans[2]=k*k

        for i in range(3,n+1):
            ans[i]=(k-1)*(ans[i-1]+ans[i-2])
        return ans[n]