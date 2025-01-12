class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        i,j=0,0
        while i<len(s) and j<len(words):
            n = len(words[j])
            if s[i:i+n] != words[j]:
                return False
            else:
                i+=n
                j+=1
        return i==len(s)