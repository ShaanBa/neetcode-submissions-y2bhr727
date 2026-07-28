class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if (num - 1) not in num_set:
                streak = 1
                while (num+1) in num_set:
                    streak += 1
                    num +=1
                if streak > longest_streak:
                    longest_streak = streak
        return longest_streak