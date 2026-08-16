class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for i in range(len(strs)):
            newStr = ''.join(sorted(strs[i]))
            if(newStr not in group):
                group[newStr] = [strs[i]]
            else:
                group[newStr].append(strs[i])

        return list(group.values())


        