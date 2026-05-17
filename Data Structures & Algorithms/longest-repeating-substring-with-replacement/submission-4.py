class Solution:
    def characterReplacement(self, s: str, k: int) -> int:    
        #update rp one step at a time while adjusting lp dynamically
    
        l = 0
        currentlen = 1
        bestlen = 1
        char_map = {}
        for i in range(0, len(s)):
            char_map[s[i]] = char_map.get(s[i], 0) + 1
            if currentlen - max(char_map.values()) <= k:
                bestlen = max(bestlen, currentlen)
            else:
                while currentlen - max(char_map.values()) > k:
                    currentlen -= 1
                    char_map[s[l]] -= 1
                    l += 1
            currentlen += 1
            print(currentlen, bestlen)
        return bestlen

   
            
        