class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # if a number appears more than once return true
        # the approach for this is pretty simple we can use a set it gets rid of duplicates for us and if the len (set(nums)) == len(num) we now its not a dupe
        return len(set(nums)) != len(nums)