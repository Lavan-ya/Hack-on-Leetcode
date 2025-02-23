class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        sets=set(nums)
        myList=list(sets)
        myList.sort()
        if len(myList)>2:
            index=len(myList)-3
            return myList[index]
        else:
            return max(myList)
            
        