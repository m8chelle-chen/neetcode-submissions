class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index = 0
        if(len(s) == 0):
            return True
        if len(s) > len(t):
            return False
        else:
            # lastIndex = 0
            # for c in s:
            #     if c not in t:
            #         return False
            #     else:
            #         lastIndex = t.find(c)
            #         t = t[lastIndex+1:]
            # return True
            for i in t:
                if(i == s[index]):
                    index += 1
                if(index == len(s)):
                    return True
            return False

