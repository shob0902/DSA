from collections import Counter
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        f=Counter(arr)
        for i in arr:
            if f[i]==1:
                k-=1
                if k==0:
                    return i
        return ""