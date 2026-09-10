class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lenNums = len(nums)

        for i in range(lenNums-1):
            for j in range(i+1,lenNums):
                if nums[i]==nums[j]:
                    return True
        return False