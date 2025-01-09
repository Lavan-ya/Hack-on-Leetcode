class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        storage ={}
        for i in range(len(nums)):
            result=target-nums[i]
            if result in storage:
                return [i,storage[result]]
            else:
                storage[nums[i]]=i
        return [-1,-1]
        