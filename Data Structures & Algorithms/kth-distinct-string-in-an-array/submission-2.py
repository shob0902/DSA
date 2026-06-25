from collections import Counter
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        f={}
        for i in arr:
            f[i]=f.get(i,0)+1
        for i in arr:
            if f[i]==1:
                k-=1
                if k==0:
                    return i
        return ""