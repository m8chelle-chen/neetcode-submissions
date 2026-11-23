class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        sum = 0
        count = 0
        prev_done = 0
        for i in customers:
            count += 1
            if prev_done > i[0]:
                prev_done = prev_done + i[1]
            else:
                prev_done = i[0] + i[1]
            sum += prev_done - i[0]
            print(prev_done, sum, i[0])

        return sum/count


        