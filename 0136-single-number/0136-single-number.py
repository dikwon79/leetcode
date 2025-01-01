class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = Counter(nums)

        for index, count in count.items():
            if count == 1:
                return index
        
        return None