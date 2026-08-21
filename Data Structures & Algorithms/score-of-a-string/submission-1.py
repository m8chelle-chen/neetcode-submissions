class Solution:
    def scoreOfString(self, s: str) -> int:
        index = 1
        sum = 0
        if(len(s) == 1):
            return 0
        while index < len(s):
            sum += abs(ord(s[index]) - ord(s[index - 1]))
            index += 1

        return sum