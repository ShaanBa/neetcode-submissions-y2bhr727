class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and (nums[i] == nums[i-1]):
                continue
            if nums[i] > 0:
                break

            L = i + 1
            R = len(nums) - 1

            while L < R:
                total = nums[i] + nums[L] + nums[R]
                if total < 0: 
                    L += 1
                elif total > 0:
                    R -= 1
                else:

                    result.append([nums[i], nums[L], nums[R]])
                    L += 1
                    R -= 1
                    while nums[L] == nums[L-1] and L < R:
                            L += 1
                    while nums[R] == nums[R+1] and L < R:
                        if L < R:
                            R -= 1            
        return result

        