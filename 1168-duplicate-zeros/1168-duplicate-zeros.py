class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        l=[0]*len(arr)
        m,r=0,0
        while m<len(arr):
            if arr[r]!=0:
                l[m]=arr[r]
            else:
                l[m]=0
                m+=1
                if m+1<len(arr):
                    l[m]=0
            m+=1
            r+=1
        arr[:]=l
        

        