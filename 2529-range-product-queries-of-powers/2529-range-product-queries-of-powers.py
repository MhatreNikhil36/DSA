class Solution:
    def getPowers(self,n:int)->List[int]:
        q=n
        binary=[]
        while q>0:
            binary.append(q%2)
            q//=2
        res=[]
        for i in  range(len(binary)):
            if binary[i]==1:
                res.append(2**i)
        return res

        


    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        mod=10**9 + 7
        powers=self.getPowers(n)
        preProducts=[]
        for x in powers:
            if not preProducts:
                preProducts.append(x)
            else:
                preProducts.append(x*preProducts[-1])
        res=[]
        for l,r in queries:
            l=l-1
            if l<0:
                res.append(int((preProducts[r])%mod))
            else:
                res.append(int((preProducts[r]/preProducts[l])%mod))

        return res

