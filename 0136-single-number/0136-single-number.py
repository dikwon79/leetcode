class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        arraycount = Counter(nums)

        for i, val in arraycount.items():
            if val == 1:
                return i
        