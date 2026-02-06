class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        distance=float('inf')
        best_sum=0
        for i in range(0,len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]: 
                continue
            l,r=i+1,len(nums)-1
            while l<r:
                sums=nums[i]+nums[l]+nums[r]
                best_dist = abs(target-sums)
                if best_dist<distance:
                    distance=best_dist
                    best_sum=sums
                if sums<target:
                    l+=1
                elif sums==target:
                    return sums
                else:
                    r-=1
        return best_sum