class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr=""
        for i in range(len(strs)):
            encodedStr += str(len(str(len(strs[i])))) + str(len(strs[i]))+ strs[i]
        
        print(encodedStr)
        return encodedStr

    def decode(self, s: str) -> List[str]:
        strs=[]
        addingString=False
        readingStrLen=False
        lenStr=0
        lenlenStr=0
        for i in range(len(s)):
            if(not addingString):
                if(readingStrLen):
                    lenStr+=s[i]
                    lenlenStr-=1
                    if(lenlenStr==0):
                        lenStr = int(lenStr)
                        if(lenStr!=0):
                            addingString=True
                        readingStrLen=False
                        strs.append("")
                else:
                    lenlenStr = int(s[i])
                    readingStrLen = True
                    lenStr=""
            else:
                strs[-1] += s[i]
                lenStr-=1
                if(lenStr==0):
                    addingString=False

        return strs
