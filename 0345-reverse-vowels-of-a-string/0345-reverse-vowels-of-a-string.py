class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=set('aeiouAEIOU')
        left=0
        right=len(s)-1
        lst=list(s)
        while left<right:
            if lst[left] in vowels and lst[right] in vowels:
                lst[left],lst[right]=lst[right],lst[left]
                left+=1
                right-=1
            elif lst[left] not in vowels and lst[right] not in vowels:
                left+=1
                right-=1
            else:
                if lst[left] not in vowels:
                    left+=1
                else:
                    right-=1
        return "".join(lst)
        