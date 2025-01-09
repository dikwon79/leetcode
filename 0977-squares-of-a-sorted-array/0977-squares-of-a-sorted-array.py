class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
         value = [ i*i for i in nums]
         return sorted(value)