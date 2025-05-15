class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph=defaultdict(set)
        ind=OrderedDict()
        for word in words:
            for c in word:
                if c not in ind:
                    ind[c] = 0
        for i in range(len(words)-1):
            a=words[i]
            b=words[i+1]

            n=min(len(a),len(b))
            if len(a) > len(b) and a.startswith(b):
                return ""
            for s in range(n):
                if a[s]!=b[s]:
                    if a[s] not in ind:
                        ind[a[s]]=0
                    if b[s] not in ind:
                        ind[b[s]]=0
                    if b[s] not in graph[a[s]]:
                        ind[b[s]]+=1
                        graph[a[s]].add(b[s])
                    break

        # print(graph,ind)
        ans=self.sortgraph(ind,graph)
        return ans
        
    
    def sortgraph(self,ind,graph:dict)->str:

        q=deque()
        for x in ind:
            if ind[x]==0:
                q.append(x)
        rem=len(ind)
        order=''
        while q:
            for i in range(len(q)):
                x=q.popleft()
                order+=x
                rem-=1
                for y in graph[x]:
                    ind[y]-=1
                    if ind[y]==0:
                        q.append(y)
        # print('final',order)
        if len(order)!=len(ind):
            return ""
        return order

