class Solution:
    def longestPalindrome(self, s: str) -> int:
        pal = {}
        count = 0
        excount = 0
        for char in s:
            if char not in pal:
                pal[char] = 1
            else:
                pal[char] += 1
        
        for key, value in pal.items():
            
            if value % 2 == 0:
                count += value
            else:
                count += value-1
                excount = 1 
           
        
        return count + (1 if excount > 0 else 0)
                
            
            