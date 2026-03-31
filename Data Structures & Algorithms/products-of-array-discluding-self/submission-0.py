class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1 for n in nums]
        for i in range(0, len(nums)):
            for j in range(0,len(nums)):
                if j != i:
                    output[i] *= nums[j]
        return output
        