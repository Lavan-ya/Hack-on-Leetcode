class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        val=0
        l,r=0,len(arr)-1
        while l<=r:
            mid=l+(r-l)//2
            val=arr[mid]-(mid+1)
            if val<k:
                l=mid+1
            else:
                r=mid-1
        ele = arr[r]-(r+1)
        return arr[r]+(k-ele)
            