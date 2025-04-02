from typing import List

class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = {i: [] for i in range(n)}
        
        # Build adjacency list
        for u, v in edges:
            graph[u].append(v)
        
        # If the destination has outgoing edges, return False immediately
        if graph[destination]: 
            return False
        
        # Node states: 0 = unvisited, 1 = visiting (GRAY), 2 = visited (BLACK)
        state = [0] * n 
        
        def dfs(node):
            if state[node] == 1:  # Cycle detected
                return False
            if state[node] == 2:  # Already processed node
                return True
            if not graph[node]:  # Leaf node
                return node == destination
            
            state[node] = 1  # Mark node as visiting (GRAY)
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            
            state[node] = 2  # Mark node as visited (BLACK)
            return True
        
        return dfs(source)
