class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        index = 0
        for i in s:
            if index < len(t) and i == t[index]:
                index += 1
            
        return len(t) - index
                
