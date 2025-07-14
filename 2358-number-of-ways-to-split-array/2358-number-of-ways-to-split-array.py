class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        p=[nums[0]]
        count=0
        for i in range(1,len(nums)):
            p.append(p[-1]+nums[i])
        
        for j in range(len(p)-1):
            firstElement=p[j]
            lastElement=p[-1]-firstElement
            if firstElement>=lastElement:
                count+=1
        return count