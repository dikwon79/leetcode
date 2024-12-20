class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        temp = Counter(nums)

        for num, count in temp.items():
            if count > 1:
                return True
        
        return False
