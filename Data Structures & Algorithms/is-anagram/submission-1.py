class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1 = {}
        map2 = {}

        for i in range(len(s)):
            map1[s[i]]= map1.get(s[i], 0) + 1
        for i in range(len(t)):
            map2[t[i]] = map2.get(t[i], 0) + 1
        print(map1, map2)
        return map1 == map2

