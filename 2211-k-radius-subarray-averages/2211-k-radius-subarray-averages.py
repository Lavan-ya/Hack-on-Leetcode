class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        lst=[-1]*len(nums)
        w=2*k + 1
        if len(nums)<w:
            return lst
        prefix=[nums[0]]
        for i in range(1,len(nums)):
            prefix.append(prefix[-1]+nums[i])
        avg=prefix[k+k]//w
        lst[k]=avg
        l=0
        for j in range(w,len(nums)):
            num=prefix[j]-prefix[l]
            lst[j-k]=num//w
            l+=1
        return lst