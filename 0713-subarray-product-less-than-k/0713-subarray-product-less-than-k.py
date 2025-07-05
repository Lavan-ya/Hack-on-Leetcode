class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans=0
        current=1
        left=0
        if k<=1:
            return 0
        for right in range(len(nums)):
            current=current*nums[right]
            while current >=k:
                current=current/nums[left]
                left+=1
            ans=ans+(right-left+1)
        return ans
        