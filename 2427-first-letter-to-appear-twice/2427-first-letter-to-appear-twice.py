class Solution:
    def repeatedCharacter(self, s: str) -> str:
        dict={}
        split_String = list(s)
        for i in range(len(split_String)):
            if split_String[i] in dict:
                dict[split_String[i]]=dict[split_String[i]]+1
                if dict[split_String[i]] >1:
                    return split_String[i]            
            else:
                dict[split_String[i]]=1