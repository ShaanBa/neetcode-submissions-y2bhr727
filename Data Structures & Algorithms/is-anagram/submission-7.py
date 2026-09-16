from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''hash1 = {}
        hash2 = {}
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] in hash1:
                hash1[s[i]] += 1
            else:
                hash1[s[i]] = 1
            
            if t[i] in hash2:
                hash2[t[i]] += 1
            else:
                hash2[t[i]] = 1
        return hash1.items() == hash2.items()

'''

        return Counter(s) == Counter(t)