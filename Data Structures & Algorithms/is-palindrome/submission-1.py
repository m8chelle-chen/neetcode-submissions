class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ''
        for i in s:
            if(i.isalpha() or i.isdigit()):
                newS += i
        newS = newS.lower()

        return newS[::-1] == newS