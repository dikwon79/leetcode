class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        temp = [i for i in range(0, len(nums)+1)]
        for key in nums:
            temp.remove(key)
        return temp[0]
        
        
