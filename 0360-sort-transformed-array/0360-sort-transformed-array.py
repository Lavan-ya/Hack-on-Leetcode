class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        lst=[]
        for num in nums:
            func= a*(num*num)+b*num+c
            lst.append(func)
        return sorted(lst)

        