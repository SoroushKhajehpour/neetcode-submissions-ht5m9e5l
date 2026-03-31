class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest_sequence = 1
        current_max = 1

        if len(nums) == 0:
            return 0
        else:
            for n in nums:
                if n-1 not in nums:
                    current_max = 1
                    i = 1
                    while (n+i) in nums:
                        current_max += 1
                        i+=1
                    if current_max > longest_sequence:
                        longest_sequence = current_max
            
            return longest_sequence

            