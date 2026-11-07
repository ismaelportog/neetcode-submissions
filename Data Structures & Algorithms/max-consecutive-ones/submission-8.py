class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_count = 0
        n = len(nums)

        for i in range(n):
            num = nums[i]
            if num == 0:
                max_count = max(max_count, count)
                count = 0
            else:
                count += 1

        return max(max_count, count)
