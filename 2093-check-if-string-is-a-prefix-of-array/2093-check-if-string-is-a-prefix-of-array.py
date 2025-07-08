class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        l,r=0,0
        while l<len(s) and r<len(words):
            count =len(words[r])
            if s[l:l+count]==words[r]:
                l+=count
                r+=1
            else:
                return False
        return len(s)==l
