class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        e=sorted(heights)
        r=0
        for i in range(len(heights)):
            if heights[i]!=e[i]:
                r+=1
        return r