class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        product_from_right, temp = {}, 1
        
        for index in range(size - 1, -1, -1):
            temp = temp * nums[index]
            product_from_right[index] = temp
        product_from_right[size] = 1

        temp = 1
        result = [0] * size
        result[0] = product_from_right[1]

        for index in range(1, size):
            temp = temp *  nums[index - 1]
            result[index] = temp * product_from_right[index + 1]

        return result


#  Approach is to calculate a prefix array from right to left and keep it in an array
#  We the iterate from left to right using a variable and multiply it with the prefix array and populate the result

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        product_from_right, product_from_left = 1, 1
        
        result = [0] * size

        for index in range(size - 1, -1, -1):
            result[index] = product_from_right
            product_from_right = product_from_right * nums[index]


        for index in range(0, size):
            result[index] *= product_from_left
            product_from_left = product_from_left * nums[index]

        return result


# Optimised Version : 
# Time Complexity - O(N) # Space Complexity  - O(1)
# Other way is to remove the prefix array, and maintain a product_from_right variable and multiply it with the result 
# Then use product_from_left and multiply it with result.  
