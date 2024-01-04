class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            key = [0]*26
            for char in s:
                key[ord(char)-97] += 1
            if str(key) in d:
                d[str(key)].append(s)
            else:
                d[str(key)] = [s]
        return d.values()