class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n=len(nums)
        m=n
        ans=[0]*(2*n)
        for i in range(n):
            ans[i]=nums[i]
            ans[m]=nums[i]
            m+=1
        return ans