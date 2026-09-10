class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numberDict = {}
        for i in range(len(nums)):
            if numberDict.get(nums[i])==None:
                numberDict[nums[i]]=1
            else:
                return True
        return False
        