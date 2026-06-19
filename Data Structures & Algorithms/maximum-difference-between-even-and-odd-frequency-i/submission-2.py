from collections import Counter
class Solution:
    def maxDifference(self, s: str) -> int:
        c=Counter(s)
        o=[]
        e=[]
        for i in c.values():
            if i%2==0:
                e.append(i)
            else:
                o.append(i)
        a=max(o)-min(e)
        return a