class Solution:
    def isHappy(self, n: int) -> bool:
        
        processed = set()

        def getnumber(n):
            value = 0

            while n:
                digit = n % 10
                value += digit **2
                n = n//10 
            return value

        while n not in processed:
            processed.add(n)
            n = getnumber(n)
            if n==1:
                return True
            
        
        return False
