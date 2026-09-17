class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0 
        hashmap = {}
        max_freq = 0
        best = 0 

        for r in range(len(s)):
            if s[r] not in hashmap:
                hashmap[s[r]] = 0
            hashmap[s[r]] += 1

            max_freq = max(max_freq, hashmap[s[r]])

            while (r - l + 1) - max_freq > k:
                hashmap[s[l]] -= 1
                l += 1
            best = max(best, r-l+1)
        return best
