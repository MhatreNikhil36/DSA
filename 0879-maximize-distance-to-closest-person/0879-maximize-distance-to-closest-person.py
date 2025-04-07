class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        # find the logest consecutieves o seq
        # if it  has 11 on both sides trhen max distance is the mid 
        # if it has 1 on just one of the sides then the max distrance is lenyh of 0 sequence
        ans=0
        lastfilled=None
        print(seats)
        for i,x in enumerate(seats):
            if x==1:
                if lastfilled!=None:
                    ans=max(ans,(i-lastfilled)//2)
                else:
                    ans=max(ans,i)
                lastfilled=i

        n=len(seats)-1
        if seats[n]!=1:
            ans=max(ans,n-lastfilled)
        return ans
                