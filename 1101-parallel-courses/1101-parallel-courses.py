class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        d=defaultdict(set)
        ind=dict()
        for i in range(1,n+1):
            ind[i]=0
        for x,y in relations:
            d[x].add(y)
            ind[y]+=1
        q=deque()

        rem=n
        for x in ind:
            if ind[x]==0:
                q.append(x)
        sem=0
        seen=set()
        while q:
            sem+=1
            n=len(q)
            for i in range(n):
                x=q.popleft()
                if ind[x]==0:
                    seen.add(x)
                    rem-=1
                    for y in d[x]:
                            ind[y]-=1
                            if ind[y]==0:
                                q.append(y)
        if rem!=0:
            return -1
        return sem
