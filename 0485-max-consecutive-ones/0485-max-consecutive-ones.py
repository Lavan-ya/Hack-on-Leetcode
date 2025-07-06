class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c,l,ans=0,0,0
        for r in range(len(nums)):
            if nums[r]==0:
                c+=1
            while c>0:
                if nums[l]==0:
                    c-=1
                l+=1
            ans=max(ans,(r-l+1))
        return ans