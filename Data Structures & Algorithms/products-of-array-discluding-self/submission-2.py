class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        swap = nums[::-1]
        result = []
        left = [0]
        right = [0]
        for i in range(len(nums)):
            if left == [0] and right == [0]:
                left.append(nums[i])
                right.append(swap[i])
            else:
                left.append(left[len(left) - 1] * nums[i])
                right.append(right[len(right) - 1] * swap[i])
        for i in range(len(nums)):
            if(i == 0):
                result.append(right[len(nums) - (i + 1)])
            elif(i == len(nums) - 1):
                result.append(left[len(nums) - 1])
            else:
                result.append(left[i] * right[len(nums) - (i + 1)])
        return result