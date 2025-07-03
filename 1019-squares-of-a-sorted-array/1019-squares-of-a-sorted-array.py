class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l =[0]*len(nums)
        i,j,k=0,len(nums)-1,len(nums)-1
        while i<=j:
            if nums[i]*nums[i] < nums[j]*nums[j]:
                l[k]=nums[j]*nums[j]
                j-=1
                k-=1
            else:
                l[k]=nums[i]*nums[i]
                i+=1
                k-=1
        return l

        