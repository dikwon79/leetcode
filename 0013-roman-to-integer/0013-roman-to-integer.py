class Solution:
    def romanToInt(self, s: str) -> int:
        hash ={
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
    
        result = 0
        for a, b in zip(s, s[1:]):
            if hash[a] < hash[b]:
                result -= hash[a]
            else:
                result += hash[a]
        result += hash[s[-1]]
        return result


        

