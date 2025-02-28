class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        dic_value = {}
        for i, value in enumerate(nums):
            if value not in dic_value:
                dic_value[value] = i
                print(dic_value)
            else:
                if abs(dic_value[value] - i) <= k:
                    return True
                else: 
                    dic_value[value] = i
        
        return False