class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l = 0 
        r = n - 1

        max_area = 0
        for i in range(l, r):
            j = len(heights) - 1
            while j > i:
                r_height = heights[j]
                l_height = heights[i]
                min_h = min(r_height, l_height)
                area = min_h * (j - i)
                if area > max_area:
                    max_area = area
                j -= 1

        return max_area
        