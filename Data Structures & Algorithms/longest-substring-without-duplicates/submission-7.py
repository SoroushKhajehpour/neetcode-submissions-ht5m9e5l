class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lp = 0
        rp = 1

        if s == "":
            return 0
        
        else: 
            seen = set()
            seen.add(s[lp])
            max_len = 1
            length = 1

        while rp < len(s) :
            if s[rp] not in seen:
                length += 1
                seen.add(s[rp])
                rp += 1
                if length > max_len:
                    max_len = length
            else:
                while s[rp] in seen:
                    seen.remove(s[lp])
                    lp += 1
                    length -= 1

        return max_len