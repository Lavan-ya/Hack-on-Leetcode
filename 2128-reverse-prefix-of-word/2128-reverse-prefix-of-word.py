class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:

        def reverse(word:str,r:int)->str:
            l=0
            lst=list(word)
            while l<r:
                lst[l],lst[r]=lst[r],lst[l]
                l+=1
                r-=1
            return "".join(lst)
        
        r=0
        while r<len(word):
            if word[r]==ch:
                return reverse(word,r)
            r+=1
        return word