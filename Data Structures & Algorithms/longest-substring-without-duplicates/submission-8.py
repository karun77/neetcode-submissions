class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        j=0

        if len(s)==0:
            return 0

        longest=1

        charsInStr = {}

        charsInStr[s[i]]=1

        while(j<len(s)-1):
            j+=1
            while(s[j] in charsInStr):
                del charsInStr[s[i]]
                i+=1
            charsInStr[s[j]]=1
            if j-i+1>longest:
                longest=j-i+1

        return longest
        