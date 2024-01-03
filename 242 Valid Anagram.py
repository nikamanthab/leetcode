def isAnagram(self, s: str, t: str) -> bool:
        # time - O(n), space - O(n)
        if len(s) != len(t): return False
        d = {}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = 1
            else:
                d[s[i]] += 1
            if t[i] not in d:
                d[t[i]] = -1
            else:
                d[t[i]] -= 1
        for i in d.keys():
            if d[i] != 0:
                return False
        return True