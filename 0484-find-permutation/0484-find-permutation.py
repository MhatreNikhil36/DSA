from typing import List
from collections import deque

class Solution:
    def findPermutation(self, s: str) -> List[int]:
        numbers = deque(range(1, len(s) + 2))
        ans = []
        n = len(s)
        i = 0

        while i < n:
            # print(i,s[i],numbers,ans)
            if s[i] == 'I':
                ans.append(numbers.popleft())

            elif s[i] == 'D':
                temp = [numbers.popleft()]
                while i < n and s[i] != 'I':
                    temp.append(numbers.popleft())
                    i += 1
                ans.extend(temp[::-1])  # Append reversed list
            i+=1
        # Append remaining numbers if any
        ans.extend(numbers)

        return ans
