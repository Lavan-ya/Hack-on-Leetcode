class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l=0
        r=len(nums)-1
        k=len(nums)-1
        ans=[0]*len(nums)
        while l<=r:
            if nums[l]*nums[l] > nums[r]*nums[r]:
                ans[k]=nums[l]*nums[l]
                k-=1
                l+=1
            else:
                ans[k]=nums[r]*nums[r]
                k-=1
                r-=1
        return ans

        