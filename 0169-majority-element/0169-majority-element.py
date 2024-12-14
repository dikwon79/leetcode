class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = Counter(nums)
        max_key = max(dic, key=dic.get) 
        return max_key