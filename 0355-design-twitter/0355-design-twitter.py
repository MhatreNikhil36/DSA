class Twitter:

    def __init__(self):
        self.follows=dict()
        self.posts=dict()
        self.logicaltime=0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.logicaltime+=1
        if userId not in self.posts:
            self.posts[userId]=[]
        self.posts[userId].append((-self.logicaltime,tweetId))
        # print('post by',userId,'at',self.posts)

    def getNewsFeed(self, userId: int) -> List[int]:
        following=None
        if userId in self.follows:
            following=self.follows[userId]
        else:
            following=[userId]

        heap=[]
        for x in following:
            if x not in self.posts:
                continue
            post=self.posts[x]
            for y in post:
                heapq.heappush(heap,y)

        ans=[]
        # print('heap',heap)
        while len(ans)<10 and heap:
            x=heapq.heappop(heap)
            ans.append(x[1])
        return ans 


        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId]=set([followerId])
        self.follows[followerId].add(followeeId)
        # print('follows',self.follows)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows and followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
        # print('unfollows',self.follows)
        
        
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)