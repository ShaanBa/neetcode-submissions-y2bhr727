class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def choose(i, curr): 
            if i == len(nums): # if we are at the end of the list 
                res.append(curr.copy()) # append a snapshot of curr to the result and return res
                return res
            curr.append(nums[i]) # add num we on to the list if we not at the end 
            choose(i+1, curr)
            curr.pop()
            choose(i+1 , curr)
        choose(0, [])

        return res