class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()
        
        for i in range(0,len(nums) - 2):
            if i > 0 and (nums[i] == nums[i-1]):
                continue
            else:
                l = i + 1
                r = len(nums) - 1
                while l < r:
                    if ((nums[i] + nums[l] + nums[r]) > 0):
                        r -= 1
                    elif ((nums[i] + nums[l] + nums[r]) < 0):
                        l += 1
                    else:
                        if ([nums[i],nums[l],nums[r]] not in triplets):
                            triplets.append([nums[i],nums[l],nums[r]])
                        r -= 1
                        l += 1

        return triplets