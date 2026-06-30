from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count=Counter(text)
        b=Counter("balloon")
        r=len(text)
        for c in b:
            r=min(r,count[c]//b[c])
        return r