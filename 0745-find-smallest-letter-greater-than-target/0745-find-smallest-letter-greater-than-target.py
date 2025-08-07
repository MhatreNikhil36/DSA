class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        res=None
        for  x in letters:
            if x>target:
                if not  res:
                    res=x
                if  x<res:
                    res=x
        if not  res:
            return letters[0]
        return res
        