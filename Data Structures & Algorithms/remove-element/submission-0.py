class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        c=nums.count(val)
        a=[x for x in nums if x!=val]
        nums[:len(a)] = a
        return len(a)