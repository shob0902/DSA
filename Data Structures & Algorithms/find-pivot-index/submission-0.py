class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(n):
            ls=rs=0
            for l in range(i):
                ls+=nums[l]
            for r in range(i+1,n):
                rs+=nums[r]
            if ls==rs:
                return i
        return -1