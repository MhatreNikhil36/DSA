class Solution:
    def calculate(self, s: str) -> int:
        num = []
        op = []
        i = 0
        n = len(s)
        operations = {'(', ')', '+', '-', '/', '*'}
        p = {'+': 1, '-': 1, '/': 2, '*': 2}

        def solve(data: list) -> int:
            # Process high priority operations first
            a = []
            b = []
            while data:
                x = data.pop(0)  # process left-to-right
                if x in operations:
                    if x in p and p[x] == 2:
                        # For multiplication or division, evaluate immediately
                        left = a.pop() if a else 0
                        right = data.pop(0)
                        if x == '*':
                            a.append(left * right)
                        else:
                            a.append(int(left / right))
                    else:
                        b.append(x)
                else:
                    a.append(x)
            # Process remaining low priority operations (addition/subtraction)
            result = a[0] if a else 0
            for idx, o in enumerate(b):
                next_val = a[idx+1]
                if o == '+':
                    result += next_val
                elif o == '-':
                    result -= next_val
            return result

        def parse_expr(i: int) -> (int, int):
            """ Recursively parse the expression starting at index i.
                Returns a tuple: (value, new_index)
            """
            tokens = []
            while i < n:
                if s[i] == ' ':
                    i += 1
                    continue
                if s[i] == '(':
                    # Recursively solve the nested expression
                    val, i = parse_expr(i + 1)
                    tokens.append(val)
                elif s[i] == ')':
                    # End of nested expression; return the evaluated result
                    return solve(tokens), i
                elif s[i] in operations:
                    tokens.append(s[i])
                else:
                    # If it's a digit, support multi-digit numbers
                    num_str = ""
                    while i < n and s[i].isdigit():
                        num_str += s[i]
                        i += 1
                    tokens.append(int(num_str))
                    continue  # already advanced i in inner loop
                i += 1
            return solve(tokens), i

        # Evaluate the entire expression starting at index 0.
        result, _ = parse_expr(0)
        return result


# # Example usage:
# sol = Solution()
# print(sol.calculate("6-4/2"))       # Expected output: 4 (i.e. 6 - (4/2) = 4)
# print(sol.calculate("6-(4/2)"))       # Expected output: 4
# print(sol.calculate("10+(2*(3+4))"))  # Expected output: 24
