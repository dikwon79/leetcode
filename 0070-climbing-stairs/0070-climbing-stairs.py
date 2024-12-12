class Solution:
    def climbStairs(self, n: int) -> int:
        a = 1
        b = 2
        value = 0
        if n == 1: 
            return a
        elif n == 2: 
            return b
        else:
            while(n - 2 > 0):
                value = a  + b
                a = b
                b = value
                n-=1
            return value
        

            


