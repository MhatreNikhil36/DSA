class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ind={}
        for i in range(numCourses):
            ind[i]=0

        graph=dict()
        for i in range(numCourses):
            graph[i]=set()
        for x,y in prerequisites:

            if y not in graph[x]:
                ind[y]+=1
            graph[x].add(y)
        print(graph)
        print(ind)
        order=self.topSort(ind,graph)
        return order[::-1] 


    def topSort(self,ind,graph):
        q=deque()
        for x in ind:
            if ind[x]==0:
                q.append(x)
        order=[]
        rem=len(ind)
        while q :
            for  i in range(len(q)):
                x=q.popleft()
                order.append(x)
                for y in graph[x]:
                    ind[y]-=1
                    if ind[y]==0:
                        q.append(y)
        if len(order)<rem:
            return []
        return order



        