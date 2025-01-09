class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        left, right = 0, len(nums) - 1
        result = [0] * len(nums)  # 결과를 저장할 배열
        write_index = len(nums) - 1  # 결과를 채울 위치를 뒤에서 부터 시작

        while left <= right:
            # 왼쪽과 오른쪽 값을 제곱한 값을 비교
            left_square = nums[left] ** 2
            right_square = nums[right] ** 2

            if left_square > right_square:
                result[write_index] = left_square
                left += 1
            else:
                result[write_index] = right_square
                right -= 1

            write_index -= 1  # 결과 배열에서 다음 위치로 이동

        return result
