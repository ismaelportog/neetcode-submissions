class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res, counter = 0,0
        for i in range(len(nums)):
            if nums[i] != 1:
                res = max(res,counter)
                counter = 0
                continue
            counter += 1
        return max(res,counter)
        