class Solution:
    def reverseBits(self, n: int) -> int:
        result = []

        while(n > 0):
            result.append(str(n % 2))
            n = n // 2
        
        print(result)
        count = 32- len(result)

        for i in range(count):
            result.append("0")

        answer = "".join(result[::])
        print(answer)

        return int(answer,2)