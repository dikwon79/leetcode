class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        sdivide = s.split()

        print(zip(pattern,sdivide))
        
        return (len(pattern) == len(sdivide)) and len(set(pattern)) == len(set(sdivide)) == len(set(zip(pattern, sdivide)))