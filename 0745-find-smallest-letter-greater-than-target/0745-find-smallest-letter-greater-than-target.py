class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        res=None
        def  find(s,e,t,arr,res=None):
            m=s+(e-s)//2
            if s>e:
                return res
            if arr[m]==t:
                print('skipping')
                while m<len(arr) and arr[m]==t:
                    print(m)
                    m+=1
                if m<len(arr):
                    return arr[m]
                else:
                    return res
            elif arr[m]<t:
                return find(m+1,e,t,arr,res)
            else:
                if not res:
                    res=arr[m]
                elif  res>arr[m]:
                    res=arr[m]
                return find(s,m-1,t,arr,res)

        n=len(letters)
        res=find(0,n-1,target,letters,None)
        if not  res:
            return letters[0]
        return res
        