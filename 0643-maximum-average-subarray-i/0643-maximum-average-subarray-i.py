class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr=0
        ans=1
        for x in range(k):
            curr=curr+nums[x]
        ans=curr/k
        for y in range(k,len(nums)):
            curr=curr+nums[y]-nums[y-k]
            avg=curr/k
            ans=max(ans,avg)
        return ans
        