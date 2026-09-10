class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output=[]
        lenNums=len(nums)

        def checkElementInArray(element,array):
            lenArray=len(array)
            if(lenArray!=0):
                lenElemArray=len(array[0])
            for i in range(lenArray):
                #assuming only 1d or 2d arrays
                count=0
                for j in range(lenElemArray):
                    if(element[j]==array[i][j]):
                        count+=1
                if(count==lenElemArray):
                    return True

            return False

        temp=0
        for i in range(lenNums-1):
            for j in range(i+1,lenNums):
                if(nums[i]>nums[j]):
                    temp=nums[i]
                    nums[i]=nums[j]
                    nums[j]=temp

        for i in range(lenNums-2):
            for j in range(i+1,lenNums-1):
                for k in range(j+1,lenNums):
                    if(checkElementInArray([nums[i],nums[j],nums[k]],output)):
                        continue
                    if((nums[i]+nums[j]+nums[k])==0):
                        output.append([nums[i],nums[j],nums[k]])
        
        return output