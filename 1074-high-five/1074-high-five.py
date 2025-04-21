class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        students={}
        id=[]
        res=[]
        for x in items:
            xId,xScore=x
            if xId not in students:
                students[xId]=[]
                heapq.heapify(students[xId])
                heapq.heappush(id,xId)
            print(xId,students[xId])
            if len(students[xId])>=5:
                if  xScore>students[xId][0]:
                    heapq.heappop(students[xId])
                    heapq.heappush(students[xId],xScore)

            else:
                heapq.heappush(students[xId],xScore)
        while id :
            i=heapq.heappop(id)
            res.append([i,sum(students[i])//5])
        return res
            



