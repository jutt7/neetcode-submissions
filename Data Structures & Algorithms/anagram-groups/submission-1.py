class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for ch in strs:
            key = ''.join(sorted(ch))
            anagrams.setdefault(key, []).append(ch)
        return list(anagrams.values())
