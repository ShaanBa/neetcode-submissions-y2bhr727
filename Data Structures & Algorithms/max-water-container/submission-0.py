class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        L = 0
        R = len(heights) - 1

        while L < R:
            width = (R - L)
            height = min(heights[L], heights[R])
            area = width * height
            if max_water < area:
                max_water = area
            
            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1
        return max_water
