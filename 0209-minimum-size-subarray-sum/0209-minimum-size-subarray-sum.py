class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,r=0,0
        ans=float('inf')
        sum=0
        while r<len(nums):
            sum+=nums[r]
            while sum>=target:
                ans=min(ans,r-l+1)
                sum-=nums[l]
                l+=1
            r+=1
        if ans==float('inf'):
            return 0
        return ans