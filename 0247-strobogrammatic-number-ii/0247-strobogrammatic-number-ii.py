class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        reversible_pairs = [
            ['0', '0'], ['1', '1'], 
            ['6', '9'], ['8', '8'], ['9', '6']
        ]

        # When n is even (n % 2 == 0), we start with strings of length 0 and
        # when n is odd (n % 2 == 1), we start with strings of length 1.
        curr_strings_length = n % 2
        
        q = ["0", "1", "8"] if curr_strings_length == 1 else [""]
        
        while curr_strings_length < n:
            curr_strings_length += 2
            next_level = []
            
            for number in q:
                for pair in reversible_pairs:
                    if curr_strings_length != n or pair[0] != '0':
                        next_level.append(pair[0] + number + pair[1])
            q = next_level
            
        return q