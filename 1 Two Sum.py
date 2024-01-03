class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # time - O(n), space - O(n)
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                return [d[nums[i]], i]
            else:
                d[target - nums[i]] = i