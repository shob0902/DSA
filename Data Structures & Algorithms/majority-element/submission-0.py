class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        for num in nums:
            c=sum(1 for i in nums if i==num)
            if c>n//2:
                return num