class Solution:
    def reverseBits(self, n: int) -> int:
        
        string = format(n,'b')
        string = string.zfill(32)
        return int(string[::-1],2)