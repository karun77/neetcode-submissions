class Solution:
    def isPalindrome(self, s: str) -> bool:
        lc_s=ord('a')
        lc_e=ord('z')
        uc_s=ord('A')
        uc_e=ord('Z')

        lenS = len(s)
        s1=""
        for i in range(lenS):
            if((ord(s[i])>=ord('0'))and(ord(s[i])<=ord('9'))):
                return False
            if((uc_s<=ord(s[i]))and(uc_e>=ord(s[i]))):
                s1=s1+chr(ord(s[i])+32)
            if(((lc_s<=ord(s[i]))and(lc_e>=ord(s[i])))):
                s1=s1+s[i]

        print(s1)

        start=0
        lenS1=len(s1)
        end=lenS1-1
        for i in range(lenS1):
            if(start>=end):
                break
            if(s1[start]!=s1[end]):
                return False
            else:
                start+=1
                end-=1

        return True



