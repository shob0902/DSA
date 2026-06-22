class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        n=len(nums)
        r=0
        for i in range(n):
            c=nums[i]
            for j in range(i+1,n):
                if nums[j]<=nums[j-1]:
                    break
                c+=nums[j]
            r=max(r,c)
        return r