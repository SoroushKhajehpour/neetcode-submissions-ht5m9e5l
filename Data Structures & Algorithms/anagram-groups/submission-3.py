class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = {}
        for word in strs:
            if ("".join(sorted(word))) not in anagrams:
                anagrams["".join(sorted(word))] = []
        
        for word in strs:
            if "".join(sorted(word)) in anagrams and word not in anagrams.values():
                anagrams["".join(sorted(word))].append(word)
        print(anagrams)
        
        anagrams_output = []
        for key in anagrams:
            anagrams_output.append(anagrams[key])
        return anagrams_output