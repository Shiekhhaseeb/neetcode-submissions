from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Create a result array filled with 1s
        res = [1] * len(nums)

        # STEP 1: Calculate products on the LEFT
        prefix = 1

        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        # STEP 2: Calculate products on the RIGHT
        postfix = 1

        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res