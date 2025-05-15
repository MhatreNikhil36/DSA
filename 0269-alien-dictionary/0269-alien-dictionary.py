from collections import defaultdict, deque
from typing import List

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = defaultdict(set)
        ind = dict()

        # Initialize all characters with in-degree 0
        for word in words:
            for c in word:
                if c not in ind:
                    ind[c] = 0

        # Build graph
        for i in range(len(words) - 1):
            a, b = words[i], words[i+1]

            # Invalid case: prefix rule
            if len(a) > len(b) and a.startswith(b):
                return ""

            for j in range(min(len(a), len(b))):
                if a[j] != b[j]:
                    if b[j] not in graph[a[j]]:
                        graph[a[j]].add(b[j])
                        ind[b[j]] += 1
                    break

        return self.sortgraph(ind, graph)

    def sortgraph(self, ind, graph: dict) -> str:
        q = deque([c for c in ind if ind[c] == 0])
        order = ''
        while q:
            c = q.popleft()
            order += c
            for nei in graph[c]:
                ind[nei] -= 1
                if ind[nei] == 0:
                    q.append(nei)

        return order if len(order) == len(ind) else ""
