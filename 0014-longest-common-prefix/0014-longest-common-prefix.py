class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s=sorted(strs)
        firstWord=s[0]
        lastWord=s[len(s)-1]
        i=0
        res=""
        if len(s)==0:
            return res
        while i<len(firstWord) and i< len(lastWord) and firstWord[i]==lastWord[i]:
            res=res+"".join(firstWord[i])
            i+=1
        return res