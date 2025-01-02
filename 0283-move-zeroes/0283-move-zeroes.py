class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        count, i = 0,0
        while(i < len(nums)):
            if nums[count] == 0:
                nums.pop(count)
                nums.append(0)
            else:
                count +=1
            i +=1
        
