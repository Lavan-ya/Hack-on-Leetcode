class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict={}
        for i in s:
            dict[i]=dict.get(i,0)+1
        for index,j in enumerate(s):
            if dict[j]==1:
                return index
        return -1
        