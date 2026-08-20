class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # dict with the smallest as key
        # value is a list of the consecutive value
        # check if the 
        hashset = set(nums)
        count = 0
        max = 0
        for i in hashset:
            count = 0
            if(i-1 not in hashset):
                consec = i
                count = 1

                while consec+1 in hashset:
                    consec += 1
                    count += 1

                if(max < count):
                    max = count

        return max                

