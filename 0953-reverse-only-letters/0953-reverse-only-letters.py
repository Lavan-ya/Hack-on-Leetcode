class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        l,r=0,len(s)-1
        lst=list(s)
        while l<r:
            if lst[l].isalpha() and lst[r].isalpha():
                lst[l],lst[r]=lst[r],lst[l]
                l+=1
                r-=1
            elif not lst[l].isalpha():
                l+=1
            else:
                r-=1
        return "".join(lst)

        