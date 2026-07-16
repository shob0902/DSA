class Solution:
    def check(self, nums: List[int]) -> bool:
        a=0
        for i in range(len(nums)):
            if nums[i]>nums[(i+1)%len(nums)]:
                a+=1
        return a<=1