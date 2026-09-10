class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater=0

        lenHeights=len(heights)

        for i in range(lenHeights-1):
            for j in range(i+1,lenHeights):
                if((min(heights[i],heights[j])*(j-i))>maxWater):
                    maxWater = min(heights[i],heights[j])*(j-i)

        return maxWater