class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def tracker(i, curr_sum, curr_combo):
            if curr_sum == target:
                res.append(curr_combo[:])
                return
            if i == len(nums):
                return
            if curr_sum > target:
                return
            
            # before we start taking we need to what do we need to do we need to 
            # maybe make a copy maybe add the place we are currently on ?
            
            curr_combo.append(nums[i])

            tracker(i, curr_sum + nums[i], curr_combo)

            curr_combo.pop()

            tracker(i+1, curr_sum, curr_combo)
        tracker(0, 0, [])
        return res
