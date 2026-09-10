class Solution:
    def trap(self, height: List[int]) -> int:
        lenHeight=len(height)
        if(lenHeight<3):
            return 0

        maxLeft=[0]*lenHeight
        maxRight=[0]*lenHeight

        for i in range(1,lenHeight-1):
            if i==1:
                maxLeft[i-1]=max(height[i-1],height[i])
            else:
                maxLeft[i-1]=max(height[i],maxLeft[i-2])

        for i in range(lenHeight-2,0,-1):
            if(i==(lenHeight-2)):
                maxRight[i-1]=max(height[i+1],height[i])
            else:
                maxRight[i-1]=max(height[i],maxRight[i])

        totalWater=0
        for i in range(lenHeight-2):
            water=(min(maxLeft[i],maxRight[i])-height[i+1])
            if water>0:
                totalWater+=water

        return totalWater

        