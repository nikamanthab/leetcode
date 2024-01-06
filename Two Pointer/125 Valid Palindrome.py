class Solution:
    def isPalindrome(self, s: str) -> bool:
        # time - O(n), space - O(0)
        s = s.lower()
        for i in s:
            if ord(i) not in list(range(ord('0'), ord('9')+1)) + list(range(ord('a'), ord('z')+1)):
                s = s.replace(i, '')
        for i in range(len(s)):
            if s[i] != s[len(s)-i-1]:
                return False
        return True