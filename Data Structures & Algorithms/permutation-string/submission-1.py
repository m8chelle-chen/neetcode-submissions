class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1 = len(s1)
        p = 0

        sub = ''
        while p + len1 <= len(s2):
            sub = s2[p:p + len1]
            for i in s1:
                if(i in sub):
                    sub = sub.replace(i, '', 1)
                else:
                    break
            if(sub == ''):
                return True
            p += 1
        
        return False
