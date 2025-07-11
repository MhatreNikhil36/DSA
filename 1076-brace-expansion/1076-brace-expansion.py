from typing import List

class Solution:
    def expand(self, s: str) -> List[str]:
        ans = []
        n = len(s)

        def trav(s, i, c):
            if i >= n:
                ans.append(c)
                return 

            if s[i] == '{':
                i += 1
                t = ''
                while s[i] != '}':
                    t += s[i]
                    i += 1
                i += 1  # move past '}'
                op = sorted(t.split(','))  # sort for lexicographical order
                for x in op:
                    trav(s, i, c + x)  # ✅ use `i`, not `i+1`
            else:
                while i < n and s[i] != '{':
                    c += s[i]
                    i += 1
                trav(s, i, c)

        trav(s, 0, '')
        return ans
