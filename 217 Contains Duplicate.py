class Solution:
    # time - O(n), space - O(n)
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = set()
        for i in nums:
            if i in d:
                return True
            else:
                d.add(i)
        return False