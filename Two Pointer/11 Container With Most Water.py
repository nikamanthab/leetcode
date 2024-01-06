class Solution:
    def maxArea(self, height: List[int]) -> int:
        # time - O(n), space - O(c)
        max_capacity = 0
        p1 = 0
        p2 = len(height)-1
        while p1 < p2:
            dist = p2 - p1
            h1, h2 = height[p1], height[p2]
            max_capacity = max(max_capacity, dist*min(h1, h2))
            if h1 > h2:
                p2-=1
            else:
                p1+=1
        return max_capacity