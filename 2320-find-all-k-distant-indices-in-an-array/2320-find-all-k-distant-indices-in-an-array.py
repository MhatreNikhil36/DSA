class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        ans=[]
        n=len(nums)
        seen=set()
        for i in range(n):
            if nums[i]==key:
                print('found at',i)
                for d in range(k+1):
                    a=i+d
                    b=i-d
                    if 0<=a<n and a not in seen:
                        seen.add(a)
                        heapq.heappush(ans,a)
                    if 0<=b<n  and b not in seen:
                        seen.add(b)
                        heapq.heappush(ans,b)
        print(ans)
        res=[]
        while ans:
            res.append(heapq.heappop(ans))
        return res
                    