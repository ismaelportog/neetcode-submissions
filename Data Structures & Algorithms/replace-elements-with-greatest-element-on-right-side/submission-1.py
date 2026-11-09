class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # [2,4,5,3,1,2]
        # create record variables for the array and max value
        n = len(arr)
        max_val = -1 # consider last position as max
        res = [0] * n

        for i in range(n-1, -1, -1):
            res[i] = max_val
            if max_val < arr[i]:
                max_val = arr[i]
        return res