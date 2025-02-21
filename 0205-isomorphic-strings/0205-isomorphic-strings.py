class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic = {}

        for sc, tc in zip(s,t):
            if sc in dic:
                if dic[sc] !=tc:
                    return False
            elif tc in dic.values():
                return False
            
            dic[sc] = tc
        
        return True