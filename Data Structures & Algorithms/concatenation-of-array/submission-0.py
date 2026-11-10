class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        cp_idx = 0
        ans = [0] * 2*n

        for i in range(len(ans)):
            ans[i] = nums[cp_idx]
            if cp_idx < n-1:
                cp_idx += 1
            else:
                cp_idx = 0

        return ans