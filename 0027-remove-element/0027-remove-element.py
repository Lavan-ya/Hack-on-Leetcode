class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        j=0
        while j<len(nums):
            if nums[j]==val:
                j+=1
            else:
                nums[i]=nums[j]
                j+=1
                i+=1
        return i
        