class Solution:
    def trap(self, height: List[int]) -> int:
        # time - O(n), Space - O(n)
        forward = []
        res = 0
        m = 0
        for i in height:
            m = max(m, i)
            forward.append(m-i)
        m = 0
        for i in range(len(height)-1, -1, -1):
            m = max(m, height[i])
            res += min(forward[i], m-height[i])
        return res
