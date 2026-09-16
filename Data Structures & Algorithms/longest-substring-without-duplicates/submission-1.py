class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        longest_streak = 0  
        l = 0 
        for r in range(len(s)):
            if s[r] in hashmap:
                while s[r] in hashmap:
                    del hashmap[s[l]]
                    l += 1
            hashmap[s[r]] = r
            longest_streak = max(longest_streak, len(hashmap))
    
        return longest_streak