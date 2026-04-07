class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for word in strs:
            alphamap = [0] * 26
            for char in word:
                lnum = ord(char) - 97
                alphamap[lnum] += 1
            tmap = tuple(alphamap)
            if tmap in hashmap:
                hashmap[tmap].append(word)
            else:
                hashmap[tmap] = [word]
        return list(hashmap.values())