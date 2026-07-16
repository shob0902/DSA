class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count={}
        for i in nums:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        for i in count.values():
            if i%2!=0:
                return False
        return True