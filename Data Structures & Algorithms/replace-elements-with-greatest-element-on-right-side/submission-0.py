class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # [2,4,5,3,1,2]
        # i = 0
        # k = 0
        # it 0
        # max = arr[i+1]
        # create sub array with the complement
        # if arr[j] > max: max replace
        # O(n^2)
        for i in range(len(arr)):
            if i == len(arr) - 1:
                arr[i] = -1
                break;

            max_val = arr[i+1]
            sub_array = arr[i+1:]
            for j in range(len(sub_array)):
                # print(f'At i = {i}, j = {j} and {arr[i+1:]} max = {max_val}')
                if max_val < sub_array[j]:
                    # print(f'{sub_array[j]} > {max_val}... swapping values')
                    max_val = sub_array[j]
                
            arr[i] = max_val
        
        return arr