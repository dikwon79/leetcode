class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic = {}
        for index in range(len(s)):
            if s[index] in dic:
                if dic[s[index]] != t[index]:
                    return False
            else:
                dic[s[index]] = t[index]
        
        return True
           