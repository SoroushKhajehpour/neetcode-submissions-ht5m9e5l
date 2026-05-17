class Solution:
    def characterReplacement(self, s: str, k: int) -> int:    
        #update rp one step at a time while adjusting lp dynamically
        #sliding window: a technique where you maintain a 
        #                   continuous section of an array/string and
        #                   move it efficiently instead of recomputing
        #                   everything from scratch.
        l = 0
        bestlen = 1
        char_map = {}
        for r in range(0, len(s)):
            char_map[s[r]] = char_map.get(s[r], 0) + 1
            if (r - l + 1) - max(char_map.values()) <= k:
                bestlen = max(bestlen, r - l + 1)
            
            else:
                while (r -l + 1) - max(char_map.values()) > k:
                    char_map[s[l]] -= 1
                    l += 1
        return bestlen

   
            
        