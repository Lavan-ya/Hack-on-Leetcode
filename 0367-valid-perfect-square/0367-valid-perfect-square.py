class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l,r=0,num-1
        while l<=r:
            mid=l+(r-l)//2
            val = mid+1
            if (val<num/val):
                l=mid+1
            elif (val>num/val):
                r=mid-1
            elif (val==num/val):
                return True
        return False
        