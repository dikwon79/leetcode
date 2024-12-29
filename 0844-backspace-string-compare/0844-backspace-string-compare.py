class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def process(value):
            temp = []

            for char in value:
                if char =="#":
                    if temp:
                        temp.pop()
                else:
                    temp.append(char)
            return temp
        
        print(process(t))
        return True if process(s) == process(t) else False