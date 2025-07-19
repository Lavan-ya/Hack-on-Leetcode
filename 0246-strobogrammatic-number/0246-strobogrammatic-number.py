class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        lst=[]
        for i in reversed(num):
            if i in {'1','0','8'}:
                lst.append(i)
            elif i =="9":
                lst.append("6")
            elif i =="6":
                lst.append("9")
            else:
                return False
        lst = "".join(lst)
        if lst==num:
            return True
        else:
            return False
        