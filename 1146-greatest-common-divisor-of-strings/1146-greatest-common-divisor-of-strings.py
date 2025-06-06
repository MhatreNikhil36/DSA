
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2!=str2+str1:
            return "" 
        def gcd(a, b):
            if a == 0:
                return b

            return gcd(b % a, a)
        
        max_length = gcd(len(str1), len(str2))
        return str1[:max_length]
        