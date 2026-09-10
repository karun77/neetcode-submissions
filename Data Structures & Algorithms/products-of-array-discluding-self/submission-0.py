class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lenNums = len(nums)
        prefixProd = [0]*lenNums
        suffixProd = [0]*lenNums
        productArr = [0]*lenNums

        prefixProd[0] = suffixProd[lenNums-1] = 1

        for i in range(1,lenNums):
            prefixProd[i] = prefixProd[i-1]*nums[i-1]
        
        for i in range(lenNums-2,-1,-1):
            suffixProd[i] = suffixProd[i+1]*nums[i+1]

        for i in range(lenNums):
            productArr[i] = prefixProd[i]*suffixProd[i]

        return productArr