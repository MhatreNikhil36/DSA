from typing import List
from collections import deque

class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        ans = []
        stack = deque()
        stack.append(([n],))  # Each item is a tuple with one list

        while stack:
            factors = list(stack.pop()[0])
            last_factor = factors.pop()

            start = factors[-1] if factors else 2

            for i in range(start, int(last_factor ** 0.5) + 1):
                if last_factor % i == 0:
                    new_factors = factors + [i, last_factor // i]
                    stack.append((new_factors,))
                    ans.append(new_factors[:])  # Add a copy to result

        return ans
