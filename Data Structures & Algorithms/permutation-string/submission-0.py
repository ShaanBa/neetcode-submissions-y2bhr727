class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = {}
        for char in s1:
            s1_freq[char] = s1_freq.get(char, 0 ) + 1
        left = 0
        hash = {}
        if len(s1) > len(s2):
            return False
        for right in range(len(s2)):
            if s2[right] in hash: 
                hash[s2[right]] += 1
            else: 
                hash[s2[right]] = 1

            if right + 1 - left > len(s1):
                hash[s2[left]] -= 1
                if hash[s2[left]] == 0:
                    del hash[s2[left]]
                left += 1

            if hash.items() == s1_freq.items():
                return True
        return False
