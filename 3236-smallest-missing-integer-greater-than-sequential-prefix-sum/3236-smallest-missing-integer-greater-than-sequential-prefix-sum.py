class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        i=1
        sums=nums[0]
        while i<len(nums) and nums[i-1]+1==nums[i]:
            sums=sums+nums[i]
            i+=1
        s=set(nums)
        while sums in s:
            sums+=1
        return sums