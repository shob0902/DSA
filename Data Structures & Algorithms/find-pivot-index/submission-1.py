class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n=len(nums)
        t=sum(nums)
        l=0
        for i in range(n):
            r=t-l-nums[i]
            if l==r:
                return i
            l+=nums[i]
        return -1