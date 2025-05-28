from collections import Counter, deque
import heapq

class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k == 0:
            return s
        
        freq = Counter(s)
        max_heap = [(-cnt, char) for char, cnt in freq.items()]
        heapq.heapify(max_heap)
        
        queue = deque()  # holds tuples of (cnt, char, available_at_time)
        result = []
        time = 0
        
        while max_heap or queue:
            if max_heap:
                cnt, char = heapq.heappop(max_heap)
                result.append(char)
                time += 1
                # If there's still more of this character, put it into cooldown
                if -cnt > 1:
                    queue.append((cnt + 1, char, time + k - 1))
            else:
                # CPU idle (no available chars)
                result.append(" ")
                time += 1

            # Check if front of queue can be pushed back to heap
            if queue and queue[0][2] == time:
                heapq.heappush(max_heap, (queue[0][0], queue[0][1]))
                queue.popleft()
        
        result_str = "".join(result)
        return result_str if len(result_str) == len(s) else ""
