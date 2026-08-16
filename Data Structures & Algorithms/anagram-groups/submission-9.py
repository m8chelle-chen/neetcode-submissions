class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for i in strs:
            newStr = ''.join(sorted(i))
            if(newStr not in group):
                group[newStr] = [i]
            else:
                group[newStr].append(i)

        return list(group.values())


        