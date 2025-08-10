class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        right=1
        left=0
        while right<len(nums):
            if nums[left]==0 and nums[right]!=0:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
            elif nums[left]!=0:
                left+=1
            right+=1