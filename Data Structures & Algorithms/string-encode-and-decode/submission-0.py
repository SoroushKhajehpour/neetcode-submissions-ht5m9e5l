class Solution:

    def encode(self, strs: List[str]) -> str:
        num_char = [str(len(i)) for i in strs]
        encoded_str = ""
        for i in range(0,len(strs)):
            encoded_str+= num_char[i] + "#" + strs[i]
        
        return encoded_str
    
    def decode(self, s: str) -> List[str]:
        res,i = [],0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            end_bound = j+1+length
            res.append(s[j+1:end_bound])
            i = end_bound
        return res