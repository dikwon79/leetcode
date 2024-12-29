class Solution:
    def countBits(self, n: int) -> List[int]:
        
        ans = []
        def count(value):
            c = 0
            while(value > 0):
                if (value % 2) > 0:
                    c += 1
                value = value // 2
            return c
        i = 0
        while(i <= n):
            ans.append(count(i))
            i += 1

        
        return ans
