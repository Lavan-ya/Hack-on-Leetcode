class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count=0
        for i in range(len(grid)):
            array = grid[i]
            l,r=0,len(array)-1
            while l<=r:
                mid = l+(r-l)//2
                if array[mid]>=0:
                    l=mid+1
                elif array[mid]<0:
                    if mid>0 and array[mid-1]<0:
                        r=mid-1
                    elif mid == 0 or array[mid - 1] >= 0:
                        count+=(len(array)-mid)
                        break;
        return count
        