class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        
        items = sorted(hashmap.items(), key=lambda item: item[1], reverse=True)


        return [item[0] for item in items[:k]]
            