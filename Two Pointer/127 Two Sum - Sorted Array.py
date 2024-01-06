class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # time - O(n), space - O(2)
        m = min(numbers)
        numbers = [i-m for i in numbers]
        target -= m+m
        for i in range(len(numbers)):
            if numbers[i] > target:
                numbers = numbers[:i]
                break
        for i in range(len(numbers)):
            for j in range(len(numbers)-1, i, -1):
                if numbers[i]+numbers[j] == target:
                    return [i+1, j+1]
                elif numbers[i]+numbers[j] < target:
                    numbers = numbers[:j+1]
                    break
        