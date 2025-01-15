class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        current_value = nums[0]
        max_value = nums[0]

        for i in range(1, len(nums)):
            current_value = max(nums[i], current_value + nums[i])
            max_value = max(max_value, current_value)
        
        return max_value

