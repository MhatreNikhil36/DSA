class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map={}
        for x in nums:
            if x not in map:
                map[x]=1
            else:
                map[x]=map[x]+1
        # print(map)
        sort= sorted(map.items(), key= lambda item:item[1], reverse=True)
        # print(sort)
        ans=[]
        for x in sort:
            if k==0:
                break
            ans.append(x[0])
            k-=1
        # print(ans)
        return ans 

