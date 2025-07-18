class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2_copy = nums2[:]       
        result = []
        for x in nums1:
            if x in nums2_copy:
                result.append(x)
                nums2_copy.remove(x)  
        return result