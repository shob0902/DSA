class Solution:
    def isValid(self, str: str) -> bool:
        s=[]
        a={")":"(","]":"[","}":"{"}
        for c in str:
            if c in a:
                if s and s[-1]==a[c]:
                    s.pop()
                else:
                    return False
            else:
                s.append(c)
        return True if not s else False