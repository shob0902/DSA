class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        mr=-1
        for i in range(len(arr)-1,-1,-1):
            c=arr[i]
            arr[i]=mr
            mr=max(mr,c)
        return arr