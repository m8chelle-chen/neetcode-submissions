class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        else:
            lastIndex = 0
            for c in s:
                if c not in t:
                    return False
                else:
                    lastIndex = t.find(c)
                    t = t[lastIndex+1:]
            return True

