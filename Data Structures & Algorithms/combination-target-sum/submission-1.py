class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def tracker(curr_sum, curr_combo, i):
            if curr_sum == target:
                res.append(curr_combo[:])
                return
            if curr_sum > target:
                return
            if i == len(nums):
                return
                

            curr_combo.append(nums[i])
            tracker(curr_sum + nums[i], curr_combo, i)

            curr_combo.pop()

            tracker(curr_sum, curr_combo, i + 1)

        tracker(0, [], 0)

        return res