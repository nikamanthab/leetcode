class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # time - O(n), space - O(n)
        arr = []
        for i in range(len(nums)+1):
            arr.append(set())
        d = {}
        res = []
        for i in nums:
            if i not in d:
                d[i] = 1
                arr[d[i]].add(i)
            else:
                d[i] += 1
                arr[d[i]].add(i)
                arr[d[i]-1].remove(i)
        total = 0
        
        for i in range(len(arr)-1, -1, -1):
            temp = arr[i]
            if len(temp)+total <= k:
                res += list(temp)
                total += len(temp)
        return res