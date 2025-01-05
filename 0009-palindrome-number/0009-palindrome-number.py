class Solution:
    def isPalindrome(self, x: int) -> bool:
        mok = x
        value = 0 
        if x < 0:
            return False
            
        while (mok > 0):
            reverse = mok % 10
            mok = mok // 10
            value = value * 10 + reverse
        
        return x == value 