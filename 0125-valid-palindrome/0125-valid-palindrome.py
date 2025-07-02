class Solution:
    def isPalindrome(self, s: str) -> bool:
        letter=s.lower()
        print(letter)
        left=0
        right=len(letter)-1
        while left<right:
            if letter[left].isalnum() and letter[right].isalnum():
                if letter[left]==letter[right]:
                    left+=1
                    right-=1
                else:
                    return False
            elif not letter[left].isalnum():
                left+=1
            else:
                right-=1
        return True