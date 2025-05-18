class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # track=uf(n)
        ind=dict()
        for i in range(n):
            ind[i]=0
        graph=dict()
        for i in range(n):
            graph[i]=set()
        if not edges :
            return [0]
        for x,y in edges:
            if y not in graph[x]:
                ind[y]+=1
            if x not in graph[y]:
                ind[x]+=1
  
            graph[x].add(y)
            graph[y].add(x)
        # for i  in range(n):
        #     # print(i,ind[i])
        ans=[]
        rem=n
        q=deque()
        for i in range(n):
            if ind[i]==1:
                q.append(i)
        while rem>2:
            rem-=len(q)
            nq=deque()
            while q:
                c=q.pop()

                n=graph[c].pop()
                graph[n].remove(c)
                if len(graph[n])==1:
                    nq.append(n)
            q=nq
        # print(ans)          
        return list(q)
    

