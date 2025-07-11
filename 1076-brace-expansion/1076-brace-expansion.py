from typing import List

class Solution:
    def expand(self, s: str) -> List[str]:
        ans = []
        n = len(s)
        i=0
        def trav(s, i, c):
            # nonlocal i  # To modify i inside the nested function
            if i >= n:
                ans.append(c)
                return
            
            if s[i] == '{':
                i += 1
                t = ''
                while s[i] != '}':
                    t += s[i]
                    i += 1  # Increment i to move through the substring t
                i += 1  # Move past the closing '}'
                op = t.split(',')
                
                for x in op:
                    trav(s, i, c + x)
                    
            else:
                while i < n and s[i] != '{':
                    c += s[i]
                    i += 1
                trav(s, i, c)
        
        trav(s, 0, '')
        return sorted(ans)  # Sorting the result as per the expected output format

# # Example usage:
# solution = Solution()
# input_str = "{a,b}c{d,e}f"
# print(solution.expand(input_str))  # Output: ['acdf', 'acef', 'bcdf', 'bcef']
