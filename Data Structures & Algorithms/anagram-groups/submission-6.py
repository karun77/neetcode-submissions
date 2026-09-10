class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs2 = []
        def func(arr):
            arr2 = ""
            temp = 'a'
            lenArr = len(arr)
            arr2 = list(arr)
            for i in range(lenArr-1):
                for j in range(i+1,lenArr):
                    if ord(arr2[i])<ord(arr2[j]):
                        temp = arr2[i]
                        arr2[i] = arr2[j]
                        arr2[j] = temp
            arr2 = "".join(arr2)
            return arr2
        
        groupNoGiven = []
        groupNo = []
        for i in strs:
            strs2.append(func(i))
            groupNoGiven.append(False)
            groupNo.append(0)

        print(strs2)

        
        lenStrs = len(strs)
        maxGroupNo = 0
        latestGroupNo=-1

        for i in range(lenStrs):
            if(groupNoGiven[i]):
                continue
            else:
                latestGroupNo += 1
                groupNo[i] = latestGroupNo
                groupNoGiven[i] = True
                
            if((i==(lenStrs-1)) and (groupNoGiven[i]==False)):
                groupNo[i]=latestGroupNo
                continue
                
            for j in range(i+1,lenStrs):
                if(not groupNoGiven[j]):
                    if(strs2[i]==strs2[j]):
                        groupNo[j] = latestGroupNo
                        groupNoGiven[j] = True


        print(groupNoGiven)
        print(latestGroupNo)
        print(groupNo)

        groupedAnagrams = []

        for i in range(latestGroupNo+1):
            groupedAnagrams.append([])
        
        print(groupedAnagrams)
        
        for i in range(lenStrs):
            groupedAnagrams[groupNo[i]].append(strs[i])

        return groupedAnagrams
