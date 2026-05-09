class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        output = []

        lp = 0
        rp = len(numbers) - 1

        while lp < rp:
            sumn = numbers[lp] + numbers[rp]
            if sumn > target:
                rp -= 1
            elif sumn < target:
                lp += 1
            else:
                 output.extend([lp + 1, rp + 1])
                 return output
