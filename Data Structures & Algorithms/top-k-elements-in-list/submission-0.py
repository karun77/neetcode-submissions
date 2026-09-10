class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        groupNo=[]
        groupNoGiven=[]
        groupNoOccurences=[]
        justValueOfGroup=[]
        lenNums = len(nums)

        for i in range(lenNums):
            groupNoGiven.append(False)
            groupNo.append(0)

        latestIndex=-1
        for i in range(lenNums):
            if groupNoGiven[i]:
                continue
            else:
                latestIndex+=1
                groupNo[i]=latestIndex
                groupNoGiven[i]=True
                groupNoOccurences.append(1)
                justValueOfGroup.append(nums[i])

            if((i==(lenNums-1)) and (not groupNoGiven[i])):
                latestIndex+=1
                groupNo[i]=latestIndex
                groupNoGiven[i]=True
                groupNoOccurences.append(1)
                justValueOfGroup.append(nums[i])
                continue  

            for j in range(i+1,lenNums):
                if(not groupNoGiven[j]):
                    if(nums[i]==nums[j]):
                        groupNo[j]=latestIndex
                        groupNoGiven[j]=True
                        groupNoOccurences[groupNo[j]]+=1

        temp=0
        sortedGroupNoOccurences=groupNoOccurences
        lenGroups=len(groupNoOccurences)
        for i in range(lenGroups-1):
            for j in range(i+1,lenGroups):
                if(sortedGroupNoOccurences[i]<sortedGroupNoOccurences[j]):
                    temp=sortedGroupNoOccurences[i]
                    sortedGroupNoOccurences[i]=sortedGroupNoOccurences[j]
                    sortedGroupNoOccurences[j]=temp
                    temp=justValueOfGroup[i]
                    justValueOfGroup[i]=justValueOfGroup[j]
                    justValueOfGroup[j]=temp

        return justValueOfGroup[0:k]




