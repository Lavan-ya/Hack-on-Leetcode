class Solution:
    def countElements(self, arr: List[int]) -> int:
        sets = set(arr)
        k=0
        for i in range(len(arr)):
            if arr[i]+1 in sets:
                k+=1
        return k

        