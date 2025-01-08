class Solution:
    def reverseBits(self, n: int) -> int:
        
        string = bin(n)[2::]

        string = string.zfill(32)
        print(string[::-1])
        return int(string[::-1],2)