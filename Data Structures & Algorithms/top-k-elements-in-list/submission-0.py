class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = {}
        for num in nums:
            if num not in num_freq:
                num_freq[num] = 1
            else:
                 num_freq[num] += 1

        sorted_num_freq = sorted(num_freq.items(), key=lambda item: item[1], reverse=True)
        top_k_freq = [key for key, _ in sorted_num_freq[:k]]
        return top_k_freq

       

        

        
        