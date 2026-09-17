class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        maxfreq = 0
        l = 0

        for r in range(len(s)):
            char = s[r]
            window_len = r-l+1

            if char in hashmap:
                hashmap[char] += 1
            else:
                hashmap[char] = 1
            
            maxfreq = max(maxfreq, hashmap[char])
        
            while window_len - maxfreq > k:
                hashmap[s[l]] -= 1
                l += 1
                window_len = r-l+1
            best = max(window_len, maxfreq)
        return best
                
                


