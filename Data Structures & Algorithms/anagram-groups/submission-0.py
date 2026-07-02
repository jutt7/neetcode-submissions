class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        sorted_list = {}
        anagrams = {}
        for i in range(0,len(strs)):
            sorted_list[''.join(sorted(strs[i]))] = ''.join(sorted(strs[i]))
        for i, ch in enumerate(strs):
            if ''.join(sorted(ch)) in sorted_list:
                 anagrams.setdefault(''.join(sorted(ch)), []).append(ch)
        return list(anagrams.values())
