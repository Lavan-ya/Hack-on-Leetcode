class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        i=0
        res=[0]*len(nums)
        r=0
        while r <len(nums)-1:
            if nums[r]!=0 and nums[r]==nums[r+1]:
                res[i]=nums[r]*2
                i+=1
                r+=1
            elif nums[r]!=0:
                res[i]=nums[r]
                i+=1
            r+=1
        
        if nums[len(nums)-1]!=0 and nums[len(nums)-1]!=nums[len(nums)-2]:
            res[i]=nums[len(nums)-1]
        return res