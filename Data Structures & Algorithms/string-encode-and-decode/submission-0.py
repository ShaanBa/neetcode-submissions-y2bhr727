class Solution:

    def encode(self, strs: List[str]) -> str:
        secret = ''
        for string in strs:
            secret += f'{len(string)}${string}'
        return secret


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            dollar_index = s.find("$", i)
            length = int(s[i:dollar_index])
            word = s[dollar_index + 1: dollar_index + 1 + length]
            res.append(word)
            i = dollar_index + 1 + length
        return res
