class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        neigh={(0,1),(1,0),(-1,0),(0,-1)}
        seen=set()
        islands=[]
        m=len(grid)
        n=len(grid[0])
        ans=0
        def dfs(x,y,offset=None,land=None):
            # print(x,y,offset,land)
            if not offset:
                offset=(x,y)
                land=set()
                land.add((0,0))
            else:
                land.add((x-offset[0],y-offset[1]))
            seen.add((x,y))
            for dx,dy in neigh:
                if 0<=x+dx<m and 0<=dy+y<n and (x+dx,y+dy) not in seen  and grid[x+dx][y+dy]==1:
                    dfs(x+dx,y+dy,offset,land)
            return land
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and (i,j) not in seen:
                    land=dfs(i,j)
                    # print(land,islands)
                    if land not in islands:
                        islands.append(land)
                        ans+=1
                    seen.add((i,j))
        
        return ans 
    