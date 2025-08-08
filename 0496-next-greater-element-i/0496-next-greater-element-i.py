class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[-1]*len(nums1)
        dict={}
        for j in range(len(nums2)):
            dict[nums2[j]]=j
        
        for i in range(len(nums1)):
            idx=dict[nums1[i]]+1
            while (idx)<len(nums2):  
                if nums1[i]<nums2[idx]:
                    ans[i]=nums2[idx]
                    break 
                idx+=1          
        return ans