from typing import List
import heapq
from collections import defaultdict, deque

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        users = dict()
        for user, time, site in zip(username, timestamp, website):
            if user not in users:
                users[user] = []
            heapq.heappush(users[user], (time, site))

        pattern = dict()

        for user in users:
            # print('counting for', user)
            sites = []
            while users[user]:
                sites.append(heapq.heappop(users[user])[1])
            
            n = len(sites)
            if n < 3:
                continue
            
            # FIXED: Generate all combinations instead of sliding window
            user_patterns = set()  # Use set to avoid counting same pattern multiple times per user
            
            for i in range(n):
                for j in range(i + 1, n):
                    for k in range(j + 1, n):
                        key = (sites[i], sites[j], sites[k])
                        # print(key)
                        user_patterns.add(key)
            
            # Count each unique pattern for this user
            for key in user_patterns:
                if key not in pattern:
                    pattern[key] = 0
                pattern[key] += 1

        if not pattern:
            return []
            
        maxc = max(pattern.values())
        maxk = None
        # print(pattern)
        
        for x in pattern:
            if pattern[x] == maxc:
                if not maxk:
                    maxk = x 
                elif x < maxk:
                    maxk = x
                    
        return list(maxk) if maxk else []