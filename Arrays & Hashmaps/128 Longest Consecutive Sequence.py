class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # time - O(n), space - O(n)
        s = set(nums)
        max_len = 0
        for i in nums:
            counter = 1
            if i-1 in s:
                continue
            while i+1 in s:
                counter += 1
                i+=1
            if counter > max_len:
                max_len = counter
        return max_len