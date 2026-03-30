class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = {}
        freq = {}

        for letter in s:
            map[letter] = map.get(letter, 0) + 1
        for letter in t:
            freq[letter] = freq.get(letter, 0) + 1

        return map == freq
        