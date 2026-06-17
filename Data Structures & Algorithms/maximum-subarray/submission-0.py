class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        res=nums[0]
        for i in range(n):
            c=0
            for j in range(i,n):
                c+=nums[j]
                res=max(res,c)
        return res
