# range  lies  form  max(weights) to sum(weights)
# verifiy if a guesed weight  capa ciuty  cna  be satified 




class Solution:

    def daysPerCapacity(self,weights,capacity):
        days=1
        w=0
        for x in weights:
            if w+x<=capacity:
                w+=x 
            else:
                days+=1
                w=x
        return days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        s=max(weights)
        e=sum(weights)
        ans=e
        while s<=e:
            m=s+(e-s)//2
            reqDays=self.daysPerCapacity(weights,m)
            print(m,reqDays)
            if reqDays>days:
                s=m+1
            else:
                ans=min(ans,m)
                e=m-1
        return ans

