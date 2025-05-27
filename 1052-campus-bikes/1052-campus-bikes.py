class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        MAX_DIST = 2000                       # 0 … 2000 inclusive
        buckets = [[] for _ in range(MAX_DIST + 1)]

        # 1. bucket all pairs
        for w, (wx, wy) in enumerate(workers):
            for b, (bx, by) in enumerate(bikes):
                d = abs(wx - bx) + abs(wy - by)
                buckets[d].append((w, b))

        ans   = [-1] * len(workers)
        taken = set()

        # 2. walk distances in increasing order
        for d in range(MAX_DIST + 1):
            for w, b in buckets[d]:
                if ans[w] == -1 and b not in taken:
                    ans[w] = b
                    taken.add(b)
                    if len(taken) == len(workers):      # all workers assigned
                        return ans
        return ans
