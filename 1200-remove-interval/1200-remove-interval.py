class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        s=toBeRemoved[0]
        e=toBeRemoved[1]
        ans=[]
        for x,y in intervals:
            if x==s and y==e:
                continue
            if x>e:
                ans.append([x,y])
            elif y<s:
                ans.append([x,y])
            elif x>=s and x<e and y>e:
                ans.append([e,y])
            elif x<=s and y>=s and y<=e:
                ans.append([x,s])
            elif x<s and y>e:
                ans.append([x,s])
                ans.append([e,y])
        # print(ans)
        return ans


