from collections import deque
import math

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return 
        
        m, n = len(rooms), len(rooms[0])
        queue = deque()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Initialize distances with inf (unreachable)
        distances = [[2147483647] * n for _ in range(m)]
        
        # Enqueue all gates (0s) and mark their distance as 0
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i, j))
                    distances[i][j] = 0
        
        # BFS to find shortest paths from gates to rooms
        while queue:
            x, y = queue.popleft()
            current_distance = distances[x][y]
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and rooms[nx][ny] != -1 and distances[nx][ny] == 2147483647:
                    distances[nx][ny] = current_distance + 1
                    queue.append((nx, ny))
        
        # Update rooms with the shortest distances found
        for i in range(m):
            for j in range(n):
                if rooms[i][j] != -1:
                    rooms[i][j] = distances[i][j]
        return rooms
