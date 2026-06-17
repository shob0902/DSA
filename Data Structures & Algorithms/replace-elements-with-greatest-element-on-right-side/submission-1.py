class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        a=[0]*len(arr)
        for i in range(len(arr)):
            rm=-1
            for j in range(i+1,len(arr)):
                rm=max(rm,arr[j])
            a[i]=rm
        return a