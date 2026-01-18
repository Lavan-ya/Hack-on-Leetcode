# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l,r=0,n-1
        while l<=r:
            mid = l +(r-l)//2
            val = isBadVersion(mid+1)
            if val==False:
                l=mid+1
            elif val==True:
                if mid!=0 and isBadVersion(mid)==False :
                    return mid+1
                elif isBadVersion(mid)==True:
                    r=mid-1
                else:
                    return mid+1