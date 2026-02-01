class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        finalAnswer=[]
        nums.sort()
        for i in range(0,len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l,r=i+1,len(nums)-1
            while l<r:
                val=nums[i]+nums[l]+nums[r]
                if val>0:
                    r-=1
                    
                elif val<0:
                    l+=1
                   
                else:
                    finalAnswer.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[r]==nums[r+1]:
                        r-=1
                    
        return finalAnswer