class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_letters={}
        t_letters={}
        for sl in s:
            if sl in s_letters:
                s_letters[sl]+=1
            else:
                s_letters[sl]=1
        for tl in t:
            if tl in t_letters:
                t_letters[tl]+=1
            else:
                t_letters[tl]=1
        
        if s_letters == t_letters :
            return True 
        else  :
            return False
