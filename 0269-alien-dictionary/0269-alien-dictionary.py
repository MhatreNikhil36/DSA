class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adjlist={c:set() for word in words for c in word}
        # print(adjlist)

        for i in range(len(words)-1):
            x=words[i]
            y=words[i+1]
            m=len(x)
            n=len(y)
            minLen=min(m,n)
            if m>n and x[:minLen]==y[:minLen]:
                # print('conditon violated ')
                return ""

            for j in range(minLen):
                if x[j]!=y[j]:
                    break
            if x[j]!=y[j]:
                adjlist[x[j]].add(y[j])
        
        visited={}
        res=[]
        def dfs(c):
            if c in visited:
                return visited[c]
            visited[c]=True
            for x in adjlist[c]:
                if dfs(x):
                    return True
            visited[c]=False
            res.append(c) 
        for c in adjlist:
            if dfs(c):
                return ""
    
        res.reverse()
        return ''.join(res) 
