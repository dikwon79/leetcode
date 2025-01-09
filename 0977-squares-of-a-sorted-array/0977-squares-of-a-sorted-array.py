class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        left, right = 0, len(nums)-1
        result = [0] * len(nums)

        input_index = len(nums)-1
        while(left <= right):
            leftsq = nums[left] ** 2
            rightsq = nums[right] ** 2

            if leftsq < rightsq:
                result[input_index] = rightsq
                right -=1
            else:
                result[input_index] = leftsq
                left +=1

            input_index -=1
        return result
