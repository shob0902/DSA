class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.helper(s,t) and self.helper(t,s)
    def helper(self,s:str,t:str)->bool:
        m={}
        for i in range(len(s)):
            if (s[i] in m) and (m[s[i]]!=t[i]):
                return False
            m[s[i]]=t[i]
        return True