class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        a=[]
        a.extend(nums)
        a.extend(nums)
        return a