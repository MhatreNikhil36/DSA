# first  find the  first  n  primes
# satrt  with the  largest   and check if the remainder  is  0  or  prime

class findPrimes:
    def __init__(self,n):
        self.primes=[]
        self.n=n
        
        
    def getPrimes(self):
        while len(self.primes)<self.n:
            if  not self.primes:
                elf.findNext(1)
            else:
                self.findNext(self.primes[-1])
        return  self.primes

    def findNext(self,start):
        s=start
        isPrime=False 
        while not isPrime:
            s+=1
            isPrime=True
            for  i in  range(2,int(math.sqrt(s))+1):
                if  s%i==0:
                    isPrime=False
        return s
                


class Solution:
    def minNumberOfPrimes(self, n: int, m: int) -> int:
        primes=[2]
        s=2
        while  len(primes)<m:
            s+=1
            f=1
            for  i in  range(2,int(math.sqrt(s))+1) :
                if s%i==0:
                    f=0
            if f==1:
                primes.append(s)
        # print(primes)

        dp=[n+1  for i in range(n+1)]
        dp[0]=0
        for i in range(1,n+1):
            for x in primes:
                if x <=i:
                    r=i%x
                    q=i//x
                    if  i%x==0:
                        dp[i]=min(dp[i],q+dp[r],dp[i-x]+1)
                    else:
                        dp[i]=min(dp[i],dp[i-x]+1)
        # for i in range (n+1):
        #     print(i,dp[i])
        if  dp[-1]>n:
            return -1
        return dp[-1]