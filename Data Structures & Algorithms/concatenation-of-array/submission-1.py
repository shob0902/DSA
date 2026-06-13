class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        a=[]
        n=len(nums)
        for i in range(n):
            a.append(nums[i])
        for i in range(n):
            a.append(nums[i])
        return a