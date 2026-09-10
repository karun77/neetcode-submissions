class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lenOfString=0
        maxLen=0
        lenS=len(s)
        startOfSubString=0
        foundDuplicateChar=False
        test=0

        for i in range(lenS):
            startOfSubString=test
            for j in range(startOfSubString,i):
                if(s[j]==s[i]):
                    test=j+1
                    lenOfString=i-j
                    foundDuplicateChar=True
                    print(str(test)+","+str(j)+","+str(i))
                    break
            if(not foundDuplicateChar):
                lenOfString+=1
            else:
                foundDuplicateChar=False
            print(lenOfString)
            maxLen=max(maxLen,lenOfString)

        return maxLen
                