from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dict=defaultdict(int)
        dict[0]=1
        ans,summ=0,0
        target=0
        for right in range(len(nums)):
            summ=summ+nums[right]
            target=summ-k
            if target in dict:
                ans=ans+dict[target]
            dict[summ]+=1
        return ans