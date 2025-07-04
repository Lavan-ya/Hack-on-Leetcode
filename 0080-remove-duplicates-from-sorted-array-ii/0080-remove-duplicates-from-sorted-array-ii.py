class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left,right,k=0,1,0
        count=1
        while(right<len(nums)):
            count=1
            while right<len(nums) and nums[left]==nums[right]  :
                count+=1
                if count<=2:
                    nums[k]=nums[left]
                    k+=1
                left+=1
                right+=1
                
            if right<len(nums) and nums[left] != nums[right]:
                nums[k]=nums[left]
                left+=1
                right+=1
                k+=1
        while left<len(nums):
            nums[k]=nums[left]
            k+=1
            left+=1
        return k    