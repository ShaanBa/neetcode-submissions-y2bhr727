class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def tracker(i, curr_sub):
            # first we do our check cases if we are at the end of the nums list
            # just append the curr_sub to the result array and then we can just return to bubble
            #up
            if i == len(nums):
                res.append(curr_sub[:]) # append a copy so we know it will not change 
                return
            
            # after that we can go down the take and skips
            
            curr_sub.append(nums[i]) # append the number to curr_sub

            tracker(i+1, curr_sub) # the take branch 

            curr_sub.pop() # reset our curr_sub array 

            tracker(i+1, curr_sub) # then take the skip timeline curr_sub branch

        tracker(0, []) # index starts at zero and start with empty array 
        return res