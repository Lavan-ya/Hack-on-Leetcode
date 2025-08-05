class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        res=[0]*len(nums)
        if a>=0:
            idx=len(nums)-1
        else:
            idx=0
        
        l,r=0,len(nums)-1
        while l<=r:
            fl=a*(nums[l]*nums[l]) + b*nums[l] + c
            fr=a*(nums[r]*nums[r]) + b*nums[r] + c

            if a>=0 and fl>=fr:
                res[idx]=fl
                idx-=1
                l+=1
            elif a>=0 and fr>fl:
                res[idx]=fr
                idx-=1
                r-=1
            elif a<0 and fl<=fr:
                res[idx]=fl
                idx+=1
                l+=1
            else:
                res[idx]=fr
                idx+=1
                r-=1
        return res