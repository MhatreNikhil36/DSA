from collections import deque

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dist = [[0]*n for _ in range(m)]
        reach = [[0]*n for _ in range(m)]
        total_buildings = 0
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    total_buildings += 1
                    q = deque([(i, j, 0)])
                    visited = [[False]*n for _ in range(m)]
                    visited[i][j] = True

                    while q:
                        x, y, d = q.popleft()
                        for dx, dy in dirs:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0 and not visited[nx][ny]:
                                visited[nx][ny] = True
                                dist[nx][ny] += d + 1
                                reach[nx][ny] += 1
                                q.append((nx, ny, d + 1))

        ans = float('inf')
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and reach[i][j] == total_buildings:
                    ans = min(ans, dist[i][j])
        return ans if ans != float('inf') else -1
