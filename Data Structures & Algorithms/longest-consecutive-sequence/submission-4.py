class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lenLongestSeq=0
        seqLen=0

        #sort in increasing order
        nums1 = nums
        lenNums=len(nums)
        temp=0
        for i in range(lenNums-1):
            for j in range(i+1,lenNums):
                if(nums1[i]>nums1[j]):
                    temp=nums1[i]
                    nums1[i]=nums1[j]
                    nums1[j]=temp
        print(nums1)

        #compute longestLenSeq
        for i in range(lenNums):
            if(i==0):
                seqLen+=1
            elif(nums1[i]==(nums1[i-1]+1)):
                seqLen+=1
            elif(nums1[i]!=nums1[i-1]):
                seqLen=1
            if(lenLongestSeq<seqLen):
                lenLongestSeq=seqLen
            print(str(seqLen)+","+str(lenLongestSeq))

        return lenLongestSeq



