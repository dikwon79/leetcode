class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        value = Counter(nums)
        max_key = max(value, key=value.get) 
        return max_key