class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
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

        s1 = func(s)
        t1 = func(t)

        if s1==t1:
            return True
        else:
            return False

