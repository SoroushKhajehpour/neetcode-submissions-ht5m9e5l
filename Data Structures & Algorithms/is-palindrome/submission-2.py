class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c for c in s if c.isalnum()).lower()
        left = 0
        right = len(s) - 1
        
        if not s:
            return True

        while s[left] == s[right]:
            if left >= right:
                return True
            left += 1
            right -= 1
        return False
            
        
        