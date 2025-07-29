class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count,ans,left=0,0,0
        for right in range(len(nums)):
            if nums[right]%2!=0:
                count+=1
            while count>k:
                if nums[left]%2!=0:
                    count-=1
                left+=1
            if count==k:
                even=0
                temp=left
                while temp < len(nums) and nums[temp]%2==0:
                    even+=1
                    temp+=1
                ans=ans+even+1
        return ans