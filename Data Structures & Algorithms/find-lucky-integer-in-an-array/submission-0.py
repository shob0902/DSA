from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        f=Counter(arr)
        r=-1
        for n,c in f.items():
            if n==c:
                r=max(r,n)
        return r