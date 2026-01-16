class Solution:
    def mySqrt(self, x: int) -> int:
        nums = [l for l in range(0,65536)]
        left=0
        right = len(nums)-1
        while left<=right:
            mid = (left+right)//2
            square=nums[mid]*nums[mid]

            if square==x:
                return nums[mid]

            if square>x:
                right=mid-1
            else:
                left=mid+1
        return right
            
        