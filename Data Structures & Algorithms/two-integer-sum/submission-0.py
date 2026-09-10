class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        outputArr = []
        lenNums = len(nums)

        for i in range(lenNums-1):
            for j in range(i+1,lenNums):
                if nums[i]+nums[j]==target:
                    outputArr.append(i)
                    outputArr.append(j)

        return outputArr