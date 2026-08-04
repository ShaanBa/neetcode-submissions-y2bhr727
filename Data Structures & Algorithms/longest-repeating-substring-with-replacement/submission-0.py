class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0 
        longest = 0 
        hash = {}
        for right in range(len(s)):
            if s[right] in hash:
                hash[s[right]] += 1
            else:
                hash[s[right]] = 1
                
            if ((right + 1 - left) - (max(hash.values())) > k):
                hash[s[left]] -= 1
                left += 1

        

            longest = max(longest, right + 1 - left)

        return longest
            
        