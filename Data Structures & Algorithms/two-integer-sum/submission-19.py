class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference  = 0
        index1 = 0
        index2 = 0
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in nums[i+1:]:
                index1 = i
                index2 = nums[i+1:].index(difference) + i + 1
                break

        return [index1, index2]