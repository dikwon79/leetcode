class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:


        # 결과를 저장할 빈 배열
        n = len(nums)
        result = [0] * n  # 최종 제곱값을 저장할 배열 (크기 n)
        
        # 투 포인터 초기화
        left = 0
        right = n - 1
        # 결과 배열의 끝에서부터 시작
        position = n - 1  # 높은 인덱스부터 채워나감
        
        while left <= right:
            left_square = nums[left] ** 2
            right_square = nums[right] ** 2
            
            if left_square > right_square:
                result[position] = left_square
                left += 1
            else:
                result[position] = right_square
                right -= 1
            
            position -= 1  # 채우는 위치를 하나씩 줄임
        
        return result
