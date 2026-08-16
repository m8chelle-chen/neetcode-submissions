class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for i in nums:
            if(i in seen):
                seen[i] += 1
            else:
                seen[i] = 1
        counts = []
        for i in seen:
            counts.append([seen[i], i])
        counts.sort(reverse = True)

        top = []
        curr = 0
        
        while len(top) < k:
            top.append(counts[curr][1])
            curr += 1

        return top
