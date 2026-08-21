class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i in range(len(nums)):
            hash[nums[i]] = i
        
        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in hash.keys():
                if hash[complement] != i:
                    return [i, hash[complement]]
